# Generated by Django 4.2.8 on 2023-12-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='production_line',
            field=models.CharField(max_length=14, verbose_name='Linha de produção'),
        ),
    ]
