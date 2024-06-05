from django.contrib import admin
from .models import Employee, Job, Users, Course, ProductionLine, DayOfWeek, Availability

admin.site.register(Users)
admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Course)
admin.site.register(ProductionLine)
admin.site.register(DayOfWeek)
admin.site.register(Availability)

