import json
import time
from typing import List, Dict, Union

from channels.generic.websocket import WebsocketConsumer
from . import models


class RuletConsumer(WebsocketConsumer):
    """
    data that can be sent to the RuletConsumer (API of RuletConsumer):
    {'state': 'chosen', 'employee_id': 123} - send employee id after chosen
    {'state': 'exit'} - department does not need employees more and left the rulet

    data that can be received from the consumer below
    {'state': 'info', 'info': 'some message to show'}
                                    - information about rulet state. for example 'now is turn of 2nd dep'
    {'state': 'chosen', 'employee_id': 12}
                                    - send employee id to all consumers to remove this employee from the choosing list
    """

    connections: List['RuletConsumer'] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.department_id = self.scope['url_route']['kwargs']['department_id']

    def connect(self):
        self.accept()
        time.sleep(1)
        RuletConsumer.connections.append(self)
        print(
            f'there is {len(RuletConsumer.connections)} connected departments now '
            f'(connect department id is {self.department_id})'
        )
        self.resolve_step({'state': 'connect'})

    def disconnect(self, code):
        RuletConsumer.connections.remove(self)
        self.resolve_step({'state': 'disconnect'})
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

        self.resolve_step(data)

    def resolve_step(self, data: Dict[str, Union[int, str]]):
        if len(models.Department.objects.filter(rulet_state='does not know')) > 0:
            self.send(json.dumps({
                'state': 'info',
                'info': "waiting departments' responses",
            }))
