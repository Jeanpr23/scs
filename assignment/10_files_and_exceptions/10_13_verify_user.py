# 10_13_verify_user.py

import json

username_file = "username.json"

try:
    with open(username_file) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(username_file, 'w') as f:
        json.dump(username, f)
    print(f"We'll remember you, {username}!")
else:
    print(f"Welcome back, {username}!")
