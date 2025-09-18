# 03_07_shrinking_guest_list.py

# My guest list
guests = ["David", "Dylan", "Raisa", "Tommy", "Steve", "Alex"]

print("Original guest list:", guests)

print("\nThe new table won't arrive in time. I can only invite two people.")

# Remove guests until only two remain
while len(guests) > 2:
    removed = guests.pop()
    print("Sorry", removed, "I can’t invite you this time.")

# Show the two guests still invited
print("\nStill invited:", guests)

# Empty the list completely
guests.clear()
print("\nFinal guest list:", guests)
