# Generated by Django 4.2.8 on 2024-01-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0022_alter_employee_phone_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Gerente', 'Gerente'), ('Supervisor', 'Supervisor'), ('Padrão', 'Padrão')], max_length=100, null=True, verbose_name='Permissão'),
        ),
    ]