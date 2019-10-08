import datetime

from django.db import models


class RuletSession(models.Model):
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'rulet session in {self.date.date()} on {self.date.time()}'


class Department(models.Model):
    RULET_STATE = (  # all departments have to allow rulet. I did it to avoid cheating when one department
                     # chose employees without notification another
        ('0', 'does not know'),    # this department is not agreed yet
        ('1', 'is in rulet'),      # this department is participating in a rulet
        ('2', 'is not in rulet'),  # this department agreed, but is not participating in a rulet
    )

    name = models.CharField(max_length=256)
    address = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rulet_state = models.CharField(max_length=1, default='0', choices=RULET_STATE)

    def __str__(self):
        return self.name


class Employee(models.Model):

    def get_employee_folder_path(employee: 'Employee', filename: str) -> str:
        return f'employees_images/{employee.first_name}_{employee.last_name}/{filename}'

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to=get_employee_folder_path)

    department = models.ForeignKey(Department, blank=True, null=True,
                                   on_delete=models.SET_NULL, related_name='employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class RuletChoice(models.Model):
    rulet_session = models.ForeignKey(RuletSession, on_delete=models.CASCADE, related_name='rulet_choices')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='rulet_choices')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='rulet_choices')

    def __str__(self):
        return f'{self.rulet_session}: {self.department} chose {self.employee}'
