# Generated by Django 4.2.8 on 2024-01-12 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0030_availablehours_employee_available_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='available_hours',
        ),
        migrations.AddField(
            model_name='availablehours',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='available_hours', to='control_panel.employee', verbose_name='Funcionário'),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Gerente', 'Gerente'), ('Supervisor', 'Supervisor'), ('Normal', 'Normal')], max_length=100, null=True, verbose_name='Permissão'),
        ),
    ]
