# 09_12_multiple_modules.py

from restaurant import Restaurant
from admin import Admin

my_restaurant = Restaurant("Pizza World", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

admin_user = Admin("Jean", "Paul")
admin_user.describe_user()
admin_user.show_privileges()