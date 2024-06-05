from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.index, name="index"),
    path('auth/login', views.login, name="login"),
    path('auth/logout/', views.logout, name="logout"),
    path('linha/criar', views.create_production_line, name="create_production_line"),
    path('linha/<slug:slug>/remover', views.remove_production_line, name="remove_production_line"),
    path('linha/<slug:slug>', views.get_production_line, name="get_production_line"),
    path('funcionarios/', views.get_employees, name="get_employees"),
    path('funcionario/<int:id>', views.get_employee, name="get-employee"),
    path('registrar/employee', views.register_employee, name="register-employee"),
    path('funcionario/<int:re>/atualizar', views.update_employee, name="update-employee"),
    path('funcionario/<int:re>/deletar', views.delete_employee, name="delete_employee"),
    path('exportar/', views.export_csv, name="export_csv"),
    path('painel', views.get_panel, name="get_panel"),
    path('perfil', views.get_profile, name="get_profile"),
    path('treinamentos/lpp', views.get_lpp, name="get_lpp"),
    path('painel/jornada', views.get_journey, name="get_journey"),
    path('segurança_e_saude', views.get_security, name="get_seguranca"),
    path('teste_usuario', views.get_teste_user, name="get_teste"),
    path('mudar_senha', views.change_password, name="change_password"),
    path('hora_extra', views.get_available_times, name="get_available_times"),
    path('auth/reset_password/', PasswordResetView.as_view(template_name='auth/password_reset_form.html'), name='password_reset'),
    path('auth/reset_password/done/', PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('auth/reset/done/', PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete')
]