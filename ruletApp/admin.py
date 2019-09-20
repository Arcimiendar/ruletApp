from django.contrib import admin
from . import models

admin.site.register(models.Department)
admin.site.register(models.Employee)
admin.site.register(models.RuletSession)
admin.site.register(models.RuletChoice)
