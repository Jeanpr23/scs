# 03_06_more_guests.py

# My guest list
guests = ["David", "Dylan", "Raisa"]

print("Original guest list:", guests)

print("\nI found a bigger table, so more people can come.")

# Add guests
guests.insert(0, "Iron man")          # Add to the beginning
guests.insert(2, "Octane")         # Add to the middle
guests.append("Mirage")            # Add to the end

print("\nUpdated guest list:", guests)

for guest in guests:
    print(f"Hey {guest}, you’re invited to the table")
