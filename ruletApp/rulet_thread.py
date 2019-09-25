from threading import Lock
from typing import List, Dict, Union, Iterable

from attr import dataclass

from . import models


class RuletThread:
    @dataclass
    class Response:
        messages: List[Dict[str, Union[str, int, bool]]]
        direction: Iterable[models.Department]

    __active_thread = None
    @classmethod
    def get_instance(cls) -> 'RuletThread':  # singleton pattern.I need it to have only one instance for all departments
        if cls.__active_thread is None:
            cls.__active_thread = RuletThread()

        return cls.__active_thread

    def __init__(self):
        self.lock = Lock()
        self.departments = []
        self.rulet_session = models.RuletSession()
        self.rulet_session.active = True
        self.rulet_session.save()
        self.department_turn: Union[models.Department, None] = None
        self.index = 0
        self.was_awaiting = True

    def resolve_message(self, message: Dict[str, Union[str, int]], department: models.Department) \
            -> List[Response]:
        """
        resolve all messages, received by consumers
        :param message: received data
        :param department: department that sent data
        :return: response and direction of send (true - send response to all, false - only to sender)
        """

        with self.lock:

            if department not in self.departments:
                self.departments.append(department)

            if message['state'] == 'exit':

                if self.departments.index(department) < self.index:
                    self.index -= 1

                department.rulet_state = models.Department.RULET_STATE[2][0]
                department.save()
                self.departments.remove(department)

                responses = []

                if len(self.departments) == 0:  # if there no departments to participate more
                    self.__deactivate_rulet_session()

                else:
                    self.index %= len(self.departments)
                    responses.append(self.Response(messages=[{'state': 'info', 'info': 'now is your turn',
                                                              'exit': False}],
                                                   direction={self.departments[self.index]}))
                    if len(self.departments) > 1:
                        responses.append(self.Response(messages=[
                            {'state': 'info', 'info': f'now is turn of {self.departments[self.index]}', 'exit': False}],
                            direction={dep for dep in self.departments if self.departments.index(dep) != self.index}))

                    self.index %= len(self.departments)  # if we removed last department index goes to the next (first)

                responses.append(
                    self.Response(messages=[{'state': 'info', 'info': 'you are not participating in the rulet',
                                             'exit': True}], direction={department}))

                return responses

            if len(models.Department.objects.filter(rulet_state=models.Department.RULET_STATE[0][0])) > 0:
                # state "does not know"
                return [self.Response(messages=[{'state': 'info', 'info': 'awaiting for allow all departments',
                                                 'exit': False}],
                                      direction=self.departments)]
            elif message['state'] == 'chosen':
                if self.departments[self.index] == department:
                    self.index += 1
                    self.index %= len(self.departments)

                    employee = models.Employee.objects.get(pk=message['employee_id'])
                    rulet_choice = models.RuletChoice()
                    rulet_choice.rulet_session = self.rulet_session
                    rulet_choice.employee = employee
                    rulet_choice.department = department
                    rulet_choice.save()

                    employee.department = department
                    employee.save()

                    if len(models.Employee.objects.filter(department=None)) == 0:
                        self.__deactivate_rulet_session()
                        return [self.Response(
                            messages=[message, {'state': 'info', 'info': 'there is no employees more. Rulet is over',
                                                'exit': True}],
                            direction=self.departments
                        )]

                    return [self.Response(
                        messages=[message, {'state': 'info',
                                            'info': f'employee {employee} was chosen by {department},'
                                                    f'now is turn of {self.departments[self.index]}',
                                            'exit': False}],
                        direction={dep for dep in self.departments if dep != self.departments[self.index]}
                    ), self.Response(
                        messages=[message, {'state': 'info', 'info': f'now is your turn', 'exit': False}],
                        direction={self.departments[self.index]}
                    )]

                else:
                    return [self.Response(messages=[
                        {'state': 'info',
                         'info': f'It is not your turn now. This turn is {self.departments[self.index]}\'s turn',
                         'exit': False}
                    ], direction={department})]
            else:
                if self.was_awaiting:
                    self.was_awaiting = False
                    return [self.Response(messages=[
                        {'state': 'info',
                         'info': 'now is your turn', 'exit': False}], direction={self.departments[self.index]}),
                        self.Response(messages=[
                            {'state': 'info',
                             'info': f'now is turn of {self.departments[self.index]}', 'exit': False}],
                            direction={dep for dep in self.departments if dep!= self.departments[self.index]}
                            )]
                else:
                    return [self.Response(messages=[
                        {'state': 'info',
                         'info': 'now is your turn' if self.departments[self.index] == department else
                                 f'now is turn of {self.departments[self.index]}', 'exit': False}
                        ], direction={department})]

    def __deactivate_rulet_session(self):
        RuletThread.__active_thread = None
        self.rulet_session.active = False

        if len(self.rulet_session.rulet_choices.all()) > 0:
            self.rulet_session.save()
        else:
            self.rulet_session.delete()

        for department in models.Department.objects.all():  # set default rulet state to all departments
            department.rulet_state = models.Department.RULET_STATE[0][0]
            department.save()
