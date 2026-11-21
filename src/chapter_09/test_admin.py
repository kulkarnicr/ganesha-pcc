# Ganesha
from admin import AdminWithPrivilegesAsAttribute

admin_user_with_privileges_instance = AdminWithPrivilegesAsAttribute('Ganesha', 'Kailas', 99, 10.6)
admin_user_with_privileges_instance.describe_user()
admin_user_with_privileges_instance.privileges.show_privileges()
