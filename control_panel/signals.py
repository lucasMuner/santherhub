from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from .models import Users, Employee, Users, Availability, DayOfWeek
from rolepermissions.roles import assign_role, clear_roles
from django.http import HttpResponse

#Sinal para atualização de papel a cada atualização de dados do funcionário
@receiver(post_save, sender=Users)
def minha_funcao_de_sinal(sender, instance, created, **kwargs):
    if not created:
        clear_roles(instance)
    if instance.role:
        assign_role(instance, instance.role.lower())

#Sinal para limpar campos inutilizados na troca de papel do funcionário
@receiver(pre_save, sender=Employee)
def clean_fields(sender, instance, **kwargs):
    if instance:
        employee = Employee.objects.filter(re=instance.re).first()
        if employee:
            employee.class_field = None
            employee.production_line.clear()

#Sinal para criação da instancia da disponibilidade de horário      
@receiver(pre_save, sender=Employee)
def create_available_hours(sender, instance, **kwargs):
    if not instance.availability:
        availability = Availability.objects.create()
        instance.availability = availability
        days_of_week_list = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        for day in days_of_week_list:
            days_of_week = DayOfWeek.objects.create(name=day, availability=availability)
            days_of_week.save()

#Sinal para deletar usuário e disponibilidade de horário, quando o funcionário for deletado
@receiver(pre_delete, sender=Employee)
def delete_user_and_availability(sender, instance, **kwargs):
    user = instance.user
    availability = instance.availability
    if user:
        user.delete()
    if availability:
        availability.delete()


       
        