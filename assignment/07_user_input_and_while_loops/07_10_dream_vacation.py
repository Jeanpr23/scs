# 07_10_dream_vacation.py

responses = {}

while True:
    name = input("What's your name? ")
    place = input("If you could visit one place, where would you go? ")
    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        break

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")
