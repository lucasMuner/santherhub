# Generated by Django 4.2.8 on 2024-01-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0044_alter_employee_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_vacations',
            field=models.DateField(blank=True, null=True, verbose_name='Data da última férias'),
        ),
    ]