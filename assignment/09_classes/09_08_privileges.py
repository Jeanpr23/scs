# 09_08_privileges.py

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = Privileges(["can add post", "can delete post", "can ban user"])

admin_user = Admin("Jean", "Paul")
admin_user.privileges.show_privileges()