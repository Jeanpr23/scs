# 07_04_pizza_toppings.py

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")
