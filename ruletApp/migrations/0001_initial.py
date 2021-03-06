# Generated by Django 2.2.5 on 2019-09-19 09:31

from django.db import migrations, models
import django.db.models.deletion
import ruletApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rulet_state', models.CharField(choices=[('0', 'does not know'), ('1', 'is in rulet'), ('2', 'is not in rulet')], default='0', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RuletSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=ruletApp.models.Employee.get_employee_folder_path)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='ruletApp.Department')),
                ('rulets', models.ManyToManyField(blank=True, related_name='employees', to='ruletApp.RuletSession')),
            ],
        ),
    ]
