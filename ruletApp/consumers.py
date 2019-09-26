import asyncio
import json
import time
from typing import List, Dict, Union

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.db import transaction

from . import models
from .rulet_thread import RuletThread


class DepartmentNotificationConsumer(AsyncWebsocketConsumer):
    """
    Socket is used to send notifications to the department on frontend like real time
    api:
    {'state': 'notification'}  - let know, that rulet is to begin
    {'state': 'participating'} - let know, that departments is participating
    {'state': 'exit'}          - let know, that last rulet session is completed
    """

    connected: List['DepartmentNotificationConsumer'] = []

    async def connect(self):
        DepartmentNotificationConsumer.connected.append(self)
        await self.accept()
        department_id = self.scope['url_route']['kwargs']['department_id']
        try:
            self.department = models.Department.objects.get(pk=department_id)
            if len(models.RuletSession.objects.filter(active=True)) > 0:
                if self.department.rulet_state == models.Department.RULET_STATE[0][0]:
                    await self.send(json.dumps({'state': 'notification'}))
                elif self.department.rulet_state == models.Department.RULET_STATE[1][0]:
                    await self.send(json.dumps({'state': 'participating'}))
        except models.Department.DoesNotExist:
            await self.close()
            DepartmentNotificationConsumer.connected.remove(self)

    async def disconnect(self, code):
        DepartmentNotificationConsumer.connected.remove(self)

    @classmethod
    async def send_message_to_all(cls, msg, state):
        for connection in cls.connected:
            connection.department = models.Department.objects.get(pk=connection.department.id)
            if connection.department.rulet_state == state:
                await connection.send(json.dumps(msg))


class RuletConsumer(WebsocketConsumer):
    """
    data that can be sent to the RuletConsumer (API of RuletConsumer):
    {'state': 'update'} - ask to send actual data about state of the rulet
    {'state': 'chosen', 'employee_id': 123} - send employee id after chosen
    {'state': 'exit'} - department does not need employees more and left the rulet

    data that can be received from the consumer below
    {'state': 'info', 'info': 'some message to show', 'exit': bool}
                                    - information about rulet state. for example 'now is turn of 2nd dep'. 'exit' -
                                      close or not connection
    {'state': 'chosen', 'employee_id': 12}
                                    - send employee id to all consumers to remove this employee from the choosing list
    """

    loop = None
    connections: List['RuletConsumer'] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.department_id = self.scope['url_route']['kwargs']['department_id']
        self.this_department: models.Department = models.Department.objects.get(pk=self.department_id)
        self.this_department.rulet_state = models.Department.RULET_STATE[1][0]
        # it means department is participating in a rulet
        self.this_department.save()
        # transaction.savepoint_commit(transaction.savepoint())

        if len(models.RuletSession.objects.filter(active=True)) == 0:
            RuletConsumer.loop = asyncio.get_event_loop()
            RuletConsumer.loop.create_task(DepartmentNotificationConsumer.send_message_to_all(
                {'state': 'notification'}, models.Department.RULET_STATE[0][0]))
            RuletConsumer.loop.create_task(DepartmentNotificationConsumer.send_message_to_all(
                {'state': 'participating'}, models.Department.RULET_STATE[1][0]))

        self.rulet_thread = RuletThread.get_instance()

    def connect(self):
        self.accept()
        RuletConsumer.connections.append(self)
        self.receive('{"state": "update"}')
        print(
            f'there is {len(RuletConsumer.connections)} connected departments now '
            f'(connect department id is {self.department_id})'
        )

    def disconnect(self, code):
        RuletConsumer.connections.remove(self)
        if len(models.RuletSession.objects.filter(active=True)) == 0:
            RuletConsumer.loop.create_task(DepartmentNotificationConsumer.send_message_to_all(
                {'state': 'exit'}, models.Department.RULET_STATE[0][0]))
            RuletConsumer.loop.create_task(DepartmentNotificationConsumer.send_message_to_all(
                {'state': 'exit'}, models.Department.RULET_STATE[1][0]))
            RuletConsumer.loop.create_task(DepartmentNotificationConsumer.send_message_to_all(
                {'state': 'exit'}, models.Department.RULET_STATE[2][0]))
        print(f'there is {len(RuletConsumer.connections)} connected departments now '
              f'(disconnect department id is {self.department_id})'
              )

    def receive(self, text_data=None, bytes_data=None):
        try:
            data: Dict = json.loads(text_data)
        except json.decoder.JSONDecodeError:
            RuletConsumer.connections.remove(self)
            self.close()
            return

        if 'state' not in data.keys():  # it means that we does not allow incorrect responses
            self.close()
            RuletConsumer.connections.remove(self)
        responses = self.rulet_thread.resolve_message(data, self.this_department)

        for response in responses:
            for connection in RuletConsumer.connections:
                if connection.this_department in response.direction:
                    for message in response.messages:
                        connection.send(json.dumps(message))
