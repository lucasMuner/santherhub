# Generated by Django 4.2.8 on 2023-12-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0003_remove_employee_last_login_remove_employee_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='leave_status',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='vacation_status',
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Férias', 'Férias'), ('Afastado', 'Afastado')], default=1, max_length=20, verbose_name='Situação'),
            preserve_default=False,
        ),
    ]
