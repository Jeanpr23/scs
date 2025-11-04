# 11_03_employee.py

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

employee = Employee("Jean", "Paul", 50000)
print(f"{employee.first_name} {employee.last_name} salary: ${employee.salary}")

employee.give_raise()
print(f"After raise: ${employee.salary}")

employee.give_raise(10000)
print(f"After another raise: ${employee.salary}")
