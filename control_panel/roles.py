from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {'get_production_lines': True,
                             'get_production_line': True,
                             'create_production_line':True,
                             'remove_production_line':True,
                             'register_employee': True,
                             'update_register':True,
                             'delete_employee':True,
                             'get_employees': True,
                             'get_employee': True,
                             'get_panel': True,
                             'get_profile': True,
                             'change_password': True,
                             'export_csv': True
                             }
    
class Gerente(AbstractUserRole):
    available_permissions = {'get_production_lines': True,
                             'get_production_line': True,
                             'create_production_line':True,
                             'register_employee':True,
                             'update_register':True,
                             'export_csv': True,
                             'get_employees': True,
                             'get_employee': True,
                             'get_panel': True,
                             'get_profile': True,
                             'change_password': True,
                             'export_csv': True}
    

class Supervisor(AbstractUserRole):
    available_permissions = {'get_production_lines': True,
                             'get_production_line': True,
                             'update_register':True,
                             'get_employees': True,
                             'get_employee': True,
                             'get_panel':True,
                             'get_profile': True,
                             'change_password': True,
                             'get_available_times': True,
                             'export_csv': True}
    

    
class Normal(AbstractUserRole):
    available_permissions = {
        'get_production_lines': True,
        'get_production_line': True,
        'get_panel':True,
        'get_profile': True,
        'change_password': True,
        'get_available_times': True
        }
    