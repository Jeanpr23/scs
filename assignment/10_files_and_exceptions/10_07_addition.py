# 10_07_addition.py

while True:
    first_number = input("Enter the first number (or 'q' to quit): ")
    if first_number.lower() == 'q':
        break

    second_number = input("Enter the second number (or 'q' to quit): ")
    if second_number.lower() == 'q':
        break

    try:
        sum_numbers = int(first_number) + int(second_number)
        print(f"The sum is: {sum_numbers}")
    except ValueError:
        print("Please enter valid numbers.")
