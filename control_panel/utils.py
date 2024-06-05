from .models import Employee

def get_informations_basic_employee(filter = None):
    employees = {}
    if filter is None:
        employees = Employee.objects.filter().order_by("first_name")
    else:
        employees = Employee.objects.filter(filter).order_by("first_name")
    employees_data = []
    for employee in employees:
        employee_data = {
            "re": employee.re,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "photo": employee.photo,
            "state": employee.state,
            "job": employee.job,
            "email": employee.email,
            "phone": employee.phone
        }
        employees_data.append(employee_data)
    return employees_data

def is_job_without_production_line(job):
    jobs = ["Diretor", "Administrador", "Aprendiz"]
    return job in jobs

def is_job_without_class(job):
    jobs = ["Diretor", "Administrador", "Gerente", "Supervisor", "Planejador", "Eletrônico", "Mecânico", "Aprendiz"]
    return job in jobs or is_tecnic(job)

def is_jobs_with_more_than_production_line(job):
    jobs = ["Gerente", "Supervisor", "Planejador", "Eletrônico", "Mecânico"]
    return job in jobs or is_tecnic(job)

def is_tecnic(job):
    variations = ["Técnico", "Téc", "Tec", "Tec.", "Téc."]
    first_word = job.split(" ")[0]
    return first_word in variations

def is_operator(job):
    variations = ["Operador", "Op.", "Op"]
    first_word = job.split(" ")[0]
    return first_word in variations

roles = ["Administrador", "Gerente", "Supervisor"]
job_hierarchy = ["Op VI", "Op V", "Op IV", "Op III", "Op II", "Op I", "Ajudante geral"]