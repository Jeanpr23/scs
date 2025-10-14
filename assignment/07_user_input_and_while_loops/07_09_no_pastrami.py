# 07_09_no_pastrami.py

orders = ['tuna','pastrami','chicken','pastrami','veggie','pastrami']
print("Sorry, we're out of pastrami.\n")

while 'pastrami' in orders:
    orders.remove('pastrami')

for order in orders:
    print(f"I made your {order} sandwich.")
