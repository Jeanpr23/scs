# 09_01_restaurant.py

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

my_restaurant = Restaurant("Pizza World", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()