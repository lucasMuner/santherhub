# Generated by Django 4.2.8 on 2024-01-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0034_employee_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='class_field',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], db_column='class', max_length=1, null=True, verbose_name='Turma'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Férias', 'Férias'), ('Afastado', 'Afastado')], max_length=10, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(choices=[('Supervisor', 'Supervisor'), ('Gerente', 'Gerente'), ('Administrador', 'Administrador'), ('Operador Produção 1', 'Operador de Produção 1'), ('Operador Produção 2', 'Operador de Produção 2'), ('Técnico Eletrônico', 'Técnico Eletrônico'), ('Mecânico de Manutenção', 'Mecânico de Manutenção'), ('Inspetor de Qualidade', 'Inspetor de Qualidade'), ('Montador de Equipamentos', 'Montador de Equipamentos'), ('Operador Máquinas CNC', 'Operador de Máquinas CNC'), ('Soldador', 'Soldador'), ('Eletricista Industrial', 'Eletricista Industrial'), ('Técnico Automação Industrial', 'Técnico em Automação Industrial')], max_length=30, verbose_name='Cargo'),
        ),
    ]
