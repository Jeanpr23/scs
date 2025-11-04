# 09_07_admin.py

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = []

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

admin_user = Admin("Jean", "Paul")
admin_user.describe_user()
admin_user.show_privileges()