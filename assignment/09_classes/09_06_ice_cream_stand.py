# 09_06_ice_cream_stand.py

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} food.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="Ice Cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor)

stand = IceCreamStand("Sweet Treats")
stand.flavor
