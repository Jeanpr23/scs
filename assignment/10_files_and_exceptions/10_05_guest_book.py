# 10_05_guest_book.py

guests = []

active = True
while active:
    name = input("Enter your name (or type 'quit' to stop): ")
    if name.lower() == 'quit':
        active = False
    else:
        guests.append(name)
        print(f"Hello, {name}! You've been added to the guest book.")

print("\nGuest Book Entries:")
for guest in guests:
    print(guest)
