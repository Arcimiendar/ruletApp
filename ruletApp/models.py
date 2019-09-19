from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


class Department(models.Model):
    RULET_STATE = (
        ('0', 'does not know'),
        ('1', 'is in rulet'),
        ('2', 'is not in rulet'),
    )

    name = models.CharField(max_length=256)
    address = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rulet_state = models.CharField(max_length=1, default='0', choices=RULET_STATE)

    def __str__(self):
        return self.name


def get_employee_folder_path(employee: 'Employee', filename: str) -> str:
    return f'employees_images/{employee.first_name}_{employee.last_name}/{filename}'


class Employee(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to=get_employee_folder_path)

    department = models.ForeignKey(Department, blank=True, null=True,
                                   on_delete=models.SET_NULL, related_name='employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# class RuletSession(models.Model):
    # active = models.BooleanField(default=False)
