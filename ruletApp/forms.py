from django import forms
from . import models


class ChoseDepartmentForm(forms.Form):
    options = forms.ChoiceField(choices=zip([department.id for department in models.Department.objects.all()],
                                            models.Department.objects.all()), label='chose department')
