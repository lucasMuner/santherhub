# Generated by Django 4.2.8 on 2024-01-13 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0032_availabletimes_delete_availablehours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availabletimes',
            name='disponible',
        ),
    ]
