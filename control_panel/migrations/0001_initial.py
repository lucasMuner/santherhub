# Generated by Django 4.2.8 on 2023-12-17 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('street', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(choices=[('Operador Produção 1', 'Operador de Produção 1'), ('Operador Produção 2', 'Operador de Produção 2'), ('Técnico Eletrônico', 'Técnico Eletrônico'), ('Mecânico de Manutenção', 'Mecânico de Manutenção'), ('Inspetor de Qualidade', 'Inspetor de Qualidade'), ('Montador de Equipamentos', 'Montador de Equipamentos'), ('Operador Máquinas CNC', 'Operador de Máquinas CNC'), ('Soldador', 'Soldador'), ('Eletricista Industrial', 'Eletricista Industrial'), ('Técnico Automação Industrial', 'Técnico em Automação Industrial')], max_length=100)),
            ],
            options={
                'verbose_name': 'Trabalho',
                'verbose_name_plural': 'Trabalhos',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_title', models.CharField(choices=[('Administrador', 'Administrador'), ('Gerente', 'Gerente'), ('Supervisor', 'Supervisor'), ('Operário', 'Operário')], max_length=100)),
            ],
            options={
                'verbose_name': 'Permissão',
                'verbose_name_plural': 'Permissões',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('re', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to='profile/')),
                ('phone', models.CharField(max_length=14)),
                ('production_line', models.CharField(max_length=14)),
                ('vacation_status', models.BooleanField(default=False)),
                ('leave_status', models.BooleanField(default=False)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='control_panel.address')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_panel.job')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_panel.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'ordering': ['first_name', 'last_name', 'email'],
            },
        ),
    ]