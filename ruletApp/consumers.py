import json
from typing import List, Dict, Union

from channels.generic.websocket import WebsocketConsumer
from . import models


class RuletConsumer(WebsocketConsumer):

    connections: List['RuletConsumer'] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.department_id = self.scope['url_route']['kwargs']['department_id']

    def connect(self):
        self.accept()
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
                'info': "waiting departments' responses"
            }))
