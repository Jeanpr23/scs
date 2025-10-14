# 07_08_deli.py

sandwich_orders = ['tuna', 'pastrami', 'chicken', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"I made your {current} sandwich.")
    finished_sandwiches.append(current)

print("\nAll sandwiches are done:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
