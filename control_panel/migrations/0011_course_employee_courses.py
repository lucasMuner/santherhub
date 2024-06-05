# Generated by Django 4.2.8 on 2023-12-22 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0010_alter_employee_class_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='courses',
            field=models.ManyToManyField(related_name='Employees', to='control_panel.course', verbose_name='Curso'),
        ),
    ]
