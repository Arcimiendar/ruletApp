import json
import time
from typing import List, Dict, Union

from channels.generic.websocket import WebsocketConsumer
from . import models
from .rulet_thread import RuletThread


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

    connections: List['RuletConsumer'] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.department_id = self.scope['url_route']['kwargs']['department_id']
        self.this_department: models.Department = models.Department.objects.get(pk=self.department_id)
        self.this_department.rulet_state = models.Department.RULET_STATE[1][0]
        # it means department is participating in a rulet
        self.this_department.save()
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
