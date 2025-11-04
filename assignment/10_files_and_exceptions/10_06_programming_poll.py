# 10_06_programming_poll.py

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    language = input("Which programming language do you like most? ")

    responses[name] = language

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, language in responses.items():
    print(f"{name} prefers {language.title()}.")