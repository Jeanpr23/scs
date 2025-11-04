# 09_09_battery_upgrade.py

class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print("Battery upgraded to 85 kWh.")
        else:
            print("Battery is already 85 kWh or larger.")

battery = Battery()
battery.describe_battery()
battery.upgrade_battery()
battery.describe_battery()