# Generated by Django 4.2.8 on 2024-01-11 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0028_alter_employee_available_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='available_hours',
        ),
        migrations.DeleteModel(
            name='AvailableHours',
        ),
    ]
