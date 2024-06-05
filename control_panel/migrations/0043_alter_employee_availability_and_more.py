# Generated by Django 4.2.8 on 2024-01-22 08:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0042_alter_employee_hire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='availability',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='control_panel.availability'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cost_center',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Centro de custo'),
        ),
    ]
