from django import forms
from . import models


class ChoseDepartmentForm(forms.Form):
    options = forms.ModelChoiceField(queryset=models.Department.objects.all(), label='chose department', initial=0)
    error_css_class = 'helper-text'
