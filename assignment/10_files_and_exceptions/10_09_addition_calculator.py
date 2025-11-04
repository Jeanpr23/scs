# 10_09_addition_calculator.py

def add_numbers(a, b):
    return a + b

while True:
    first = input("Enter the first number (or 'q' to quit): ")
    if first.lower() == 'q':
        break

    second = input("Enter the second number (or 'q' to quit): ")
    if second.lower() == 'q':
        break

    try:
        result = add_numbers(int(first), int(second))
        print(f"The sum is: {result}")
    except ValueError:
        print("Please enter valid numbers.")
