# 09_04_number_served.py

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} food.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, amount):
        self.number_served += amount

restaurant = Restaurant("Jean’s Diner", "Italian")
restaurant.describe_restaurant()

restaurant.set_number_served(10)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(5)
print(f"Updated customers served: {restaurant.number_served}")