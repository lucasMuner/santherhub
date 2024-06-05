from django import forms
from .models import Employee, Job, Users, Course, ProductionLine, DayOfWeek, Availability
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from rolepermissions.decorators import has_role
from .utils import *
from django.utils.text import slugify

#Formulário para login do funcionário
class LoginForm(AuthenticationForm):
    class Meta:
        model = Users
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

#Formulário para registro de funcionário
class EmployeeForm(forms.ModelForm):
    role = forms.ChoiceField(
        choices=Users.ROLE_CHOICES,
        label="Permissão",
        widget=forms.Select(attrs={'class': 'input-primary select-role'}),
        required=False
    )
    password = forms.CharField(
        label="Senha", 
        widget=forms.TextInput(attrs={'class': 'input-primary input-password'}))
    

    class Meta:
        model = Employee
        exclude = ['user', 'available_hours', 'availability']
        widgets = {
            'courses': forms.CheckboxSelectMultiple(),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
            'last_vacations': forms.DateInput(attrs={'type': 'date'})
    }
        

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EmployeeForm, self).__init__(*args, **kwargs)
        if user:
            if has_role(user, ["gerente"]):
                self.fields["role"].choices = [
                    ('Supervisor', 'Supervisor'),
                    ('Normal', 'Normal')
                ]
                choices = self.fields["job"].choices
                new_choice = []
                for (key, value) in choices:
                    if value not in ["Diretor", "Administrador", "Gerente"]:
                        new_choice.append((key, value))
                self.fields["job"].choices = new_choice
        self.setup_fields()

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8 and password != "":
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        
        return password


    def clean(self):
        cleaned_data = super().clean()
        job = cleaned_data.get("job")
        class_field =  cleaned_data.get("class_field")
        production_lines = cleaned_data.get("production_line")
        role = cleaned_data.get("role")

        
        if str(job) in roles + ["Diretor"]:
            self.cleaned_data["role"] = "Administrador" if str(job) == "Diretor" else str(job)
            role = self.cleaned_data["role"]

        
        if role is None or role == "":
            self.add_error('role', 'Campo obrigatório.')

        if job:
            job = job.job_title
            if job in roles + ["Diretor"]:
                if role is not None:
                    if role != job and (job == "Diretor" and role != "Administrador"):
                        self.add_error('role', f'Funcionário com cargo de {job} não pode ter permissão {role}')
                    elif job == "Diretor" and role != "Administrador":
                        self.add_error('role', f'Funcionário com cargo de {job} não pode ter permissão {role}')
    
            if is_job_without_class(job) and class_field is not None:
                
                self.add_error('class_field', f'Funcionário com cargo de {job} não pode estar vinculado a uma turma')
                
            elif not is_job_without_class(job) and class_field is None:
            
                self.add_error('class_field', f'Funcionário com cargo de {job} deve estar vinculados a uma turma.')

            if is_job_without_production_line(job) and len(production_lines) > 0:
                self.add_error('production_line', f'Funcionário com cargo de {job} não pode ter vinculo com nenhuma linha.')

            if not is_jobs_with_more_than_production_line(job) and len(production_lines) > 1:
                self.add_error('production_line', f"Funcionário com cargo de {job} não pode estar vinculado em mais de uma linha.")
                

        return cleaned_data
            


    def setup_fields(self):
        self.setup_field('street', 'input-primary bg-zinc-200')
        self.setup_field('neighborhood', 'input-primary bg-zinc-200')
        self.setup_field('courses', 'rounded-md border-none checkbox-course')
        self.setup_field('class_field', 'input-primary bg-zinc-200 input-class')
        self.setup_field('job', 'input-primary bg-zinc-200 select-job')
        self.setup_field('production_line', 'input-primary bg-zinc-200 select-production-line')
        self.setup_field('phone', 'input-primary bg-zinc-200 input-phone')

        for field_name, field in self.fields.items():
            if field_name not in ['id', 'street', 'neighborhood', 'courses', 'class_field', 'job', 'phone', 'role', 'production_line', 'password']:
                self.setup_field_default(field)

    def setup_field(self, field_name, css_class):
        if field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': css_class})
            self.fields[field_name].widget.attrs['autocomplete'] = 'off'

    def setup_field_default(self, field):
        field.widget.attrs.update({'class': 'input-primary'})
        field.widget.attrs['autocomplete'] = 'off'

    def save(self, commit=True):
        user = self.instance.user
        if user:

            if user.first_name != self.cleaned_data["first_name"]:
                user.first_name = self.cleaned_data["first_name"]
                user.save()
            if user.last_name != self.cleaned_data["last_name"]:
                user.last_name = self.cleaned_data["last_name"]
                user.save()
            
            if user.email != self.cleaned_data["email"]:
                user.email = self.cleaned_data["email"]
                user.save()
            if 'password' in self.cleaned_data:
                password = self.cleaned_data["password"]
                if not user.check_password(password) and password != "":
                
                    user.set_password(password)
                    user.save()

            if user.role != self.cleaned_data["role"]:
                user.role = self.cleaned_data["role"]
                user.save()

        return super(EmployeeForm, self).save(commit)
    
#Formulário para ataulização de dados do funcionário
class UpdateEmployeeForm(EmployeeForm):

    class Meta(EmployeeForm.Meta):
        exclude = ['user', 're', 'availability', 'hire_date']

    def __init__(self, *args, **kwargs):
        super(UpdateEmployeeForm, self).__init__(*args, **kwargs)
        self.fields["password"].required = False



#Formulário para filtragem de funcionários
class FilterEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['state', 'class_field']
        widgets = {
            'state': forms.Select(),
            'class_field': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super(FilterEmployeeForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input-primary'})
            field.required = False

#Formulário para alteração de senha
class CustomSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)

        for label, field in self.fields.items():

            field.widget.attrs.update({'class': 'input-primary'})

#Formulário para a informar a disponibilidade para hora extra
class DayOfWeekForm(forms.ModelForm):
    class Meta:
        model = DayOfWeek
        exclude = ["name", "employee", "availability"]

    def __init__(self, *args, **kwargs):
        super(DayOfWeekForm, self).__init__(*args, **kwargs)

        self.fields["initial_time"].widget = forms.TimeInput(format="%H:%M", attrs={'class': 'input-primary w-full', 'type': 'time'})
        self.fields["end_time"].widget = forms.TimeInput(format="%H:%M", attrs={'class': 'input-primary w-full', 'type': 'time'})

DayOfWeekFormset = inlineformset_factory(Availability, DayOfWeek, form=DayOfWeekForm, extra=0, can_delete=False)

#Formulário de perfil a nível de adm
class myDataAdmForm(UpdateEmployeeForm):

    class Meta(EmployeeForm.Meta):
        exclude = ['user', 're', 'availability','password', 'hire_date', 'last_vacations']
    
    def __init__(self, *args, **kwargs):
        super(myDataAdmForm, self).__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields.pop('password')

        
# Formulário de perfil para funcionário, com excessão do adm
class myDataForm(myDataAdmForm):

    class Meta(myDataAdmForm.Meta):
        exclude = ['user', 're', 'availability','password', 'hire_date', 'last_vacations']
    
    def __init__(self, *args, **kwargs):
        super(myDataForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            current_class = self.fields[field_name].widget.attrs["class"]
            if field_name == "courses":
                self.fields[field_name].widget.attrs={'class': f"{current_class} primary", 'disabled': 'True'}
                continue
            self.fields[field_name].widget.attrs={'class': f'{current_class} input-primary input-disabled', 'disabled': 'True'}

# Formulário para a criação das linhas de produção
class ProductionLineForm(forms.ModelForm):

    class Meta:
        model = ProductionLine
        fields = ['name']

    def clean(self):
        cleaned_data = super().clean()
        name_production_line = cleaned_data.get("name")

        production_line_exists = ProductionLine.objects.filter(slug=slugify(name_production_line)).exists()

        if production_line_exists:
            self.add_error("name", "Linha já existente!")

        return cleaned_data


# Formulário de nível de supervisor para troca de turma e linha
class UpdateEmployeeSupervisorForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['production_line', 'class_field']

    def __init__(self, *args, **kwargs):
        super(UpdateEmployeeSupervisorForm, self).__init__(*args, **kwargs)
        
        self.fields['class_field'].widget.attrs={'class': 'input-primary select-production-line'}
        self.fields['production_line'].widget.attrs={'class': 'input-primary input-class'}
            
    def clean(self):
        cleaned_data = super().clean()
        class_field =  cleaned_data.get("class_field")
        production_lines = cleaned_data.get("production_line")

        if self.instance:
            job = self.instance.job.job_title
            if is_job_without_class(job) and class_field is not None:
                
                self.add_error('class_field', f'Funcionário com cargo de {job} não pode estar vinculado a uma turma')
                
            elif not is_job_without_class(job) and class_field is None:
            
                self.add_error('class_field', f'Funcionário com cargo de {job} deve estar vinculados a uma turma.')

            if is_job_without_production_line(job) and len(production_lines) > 0:
                self.add_error('production_line', f'Funcionário com cargo de {job} não pode ter vinculo com nenhuma linha.')

            if not is_jobs_with_more_than_production_line(job) and len(production_lines) > 1:
                self.add_error('production_line', f"Funcionário com cargo de {job} não pode estar vinculado em mais de uma linha.")


        return cleaned_data



        
        
        











    
    