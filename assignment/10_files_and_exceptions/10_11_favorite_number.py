# 10_11_favorite_number.py

import json

filename = "favorite_number.json"

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print(f"We'll remember your favorite number: {favorite_number}")
else:
    print(f"Your favorite number is {favorite_number}.")
