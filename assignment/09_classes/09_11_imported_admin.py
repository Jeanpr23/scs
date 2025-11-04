# 09_11_imported_admin.py

from admin import Admin  # assuming admin.py exists with the Admin class

admin_user = Admin("Jean", "Paul")
admin_user.describe_user()
admin_user.show_privileges()