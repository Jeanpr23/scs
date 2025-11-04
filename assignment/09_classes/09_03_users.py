# 09_03_users.py

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.city}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

user1 = User("Jean", "Paul", 19, "Reading")
user2 = User("Maria", "Lopez", 22, "New York")
user3 = User("David", "Chen", 25, "Los Angeles")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()