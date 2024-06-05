from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from .validator import validate_phone_number
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.utils.text import slugify




class Job(models.Model):
    JOB_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Ajudante geral', 'Ajudante geral'),
        ('Aprendiz', 'Aprendiz'),
        ('Diretor', 'Diretor'),
        ('Eletrônico', 'Eletrônico'),
        ('Engenheiro Eletrônico', 'Engenheiro Eletrônico'),
        ('Estagiário', 'Estagiário'),
        ('Gerente', 'Gerente'),
        ('Mecânico', 'Mecânico'),
        ('Op produção I', 'Op produção I'),
        ('Op produção II', 'Op produção II'),
        ('Op produção III', 'Op produção III'),
        ('Op produção IV', 'Op produção IV'),
        ('Op produção V', 'Op produção V'),
        ('Op produção VI', 'Op produção VI'),
        ('Planejador', 'Planejador'),
        ('Técnico mecânico','Técnico mecânico'),
        ('Técnico de processo', 'Técnicos de processo'),
        ('Supervisor', 'Supervisor'),
        ('Sup produção', 'Sup produção')
    ]
    job_title = models.CharField(max_length=30, choices=JOB_CHOICES, verbose_name="Cargo")

    class Meta:
        verbose_name="Trabalho"
        verbose_name_plural="Trabalhos"

    def __str__(self):
        return self.job_title


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ("Administrador", "Administrador"),
        ("Gerente", "Gerente"),
        ("Supervisor", "Supervisor"),
        ("Normal", "Normal")
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, verbose_name="Nome")
    last_name = models.CharField(max_length=30, verbose_name="Sobrenome")
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, verbose_name="Permissão", null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        
    def __str__(self):
        return self.email
    
class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
    
class ProductionLine(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nome", unique=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="Data de criação")

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name="Linha"
        verbose_name_plural="Linhas"

    def __str__(self):
        return self.name
    
class Availability(models.Model):
    availability_filled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = "Disponibilidade"

     
class Employee(models.Model):
    STATE_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Férias', 'Férias'),
        ('Afastado', 'Afastado')
    ]
    CLASS_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    ]
    
    re = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, verbose_name="Nome")
    last_name = models.CharField(max_length=30, verbose_name="Sobrenome")
    hire_date = models.DateField(blank=True, verbose_name="Data de contratação")
    last_vacations = models.DateField(null=True, blank=True, verbose_name="Data da última férias")
    photo = models.ImageField(upload_to="profile/", verbose_name="Foto", validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    phone = models.CharField(max_length=15, verbose_name="Telefone", validators=[validate_phone_number])
    cost_center = models.IntegerField(verbose_name="Centro de custo", validators=[MinValueValidator(0)])
    state = models.CharField(max_length=10, choices=STATE_CHOICES, verbose_name="Situação")
    class_field = models.CharField(max_length=1, choices=CLASS_CHOICES, db_column="class", verbose_name="Turma", null=True, blank=True) 
    street = models.CharField(max_length=100, verbose_name="Rua")
    neighborhood = models.CharField(max_length=50, verbose_name="Bairro")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Cargo")
    production_line = models.ManyToManyField(ProductionLine, related_name="employees", verbose_name="Linha", blank=True, null=True)
    user = models.OneToOneField(Users, on_delete=models.SET_NULL, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name="Employees", verbose_name="Curso", blank=True)
    availability = models.OneToOneField(Availability, on_delete=models.SET_NULL, null=True)
    

    class Meta:
        ordering = ["first_name", "last_name", "email"]
        verbose_name="Funcionário"
        verbose_name_plural="Funcionários"

    def __str__(self):
        return f"{self.re} - {self.first_name} {self.last_name}"
    

class DayOfWeek(models.Model):
    name = models.CharField(max_length=15, verbose_name="Dia")
    initial_time = models.TimeField(null=True, blank=True, default=None)
    end_time = models.TimeField(null=True, blank=True, default=None)
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE, related_name="days")
    

    class Meta:
        verbose_name_plural = "Dia da semana"


    def __str__(self):
        return f"{self.name} - {self.initial_time} x {self.end_time}"
    

    




    

