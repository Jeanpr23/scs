# 04_11_my_pizzas_your_pizzas.py

my_pizzas = ["pepperoni", "cheese", "bbq chicken"]
friend_pizzas = my_pizzas[:]  # a copy

my_pizzas.append("veggie")
friend_pizzas.append("margherita")

print("My pizzas:", my_pizzas)
print("Friend's pizzas:", friend_pizzas)