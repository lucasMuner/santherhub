# Generated by Django 4.2.8 on 2024-01-12 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0029_remove_employee_available_hours_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=15, verbose_name='Dia')),
                ('initial', models.TimeField(blank=True, default=None, null=True)),
                ('end', models.TimeField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'Horários disponivéis',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='available_hours',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='control_panel.availablehours'),
        ),
    ]
