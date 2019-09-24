from django import forms
from . import models
from django.utils.functional import lazy


class ChoseDepartmentForm(forms.Form):
    options = forms.ModelChoiceField(queryset=models.Department.objects.all(), label='chose department')
    error_css_class = 'helper-text'
