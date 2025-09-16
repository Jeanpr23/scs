# 03_02_greetings.py

# Ask for the user's name
name = input("What is your name? ")

# Ask for their favorite game
favorite_game = input("What's your favorite game? ")

# Ask if it's a good game
answer = input(f"Is {favorite_game}, {name}, a good game? (yes/no) ")

# Simple response
if answer.lower() == "yes":
    print("Great!")
else:
    print("Got it!")
