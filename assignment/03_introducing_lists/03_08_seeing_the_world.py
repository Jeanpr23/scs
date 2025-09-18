# 03_08_seeing_the_world.py

# Places I want to visit
places = ["California", "Chicago", "Montana", "Mexico", "Chile"]

print("Original order:", places)
print("Alphabetical order:", sorted(places))
print("Still original order:", places)

print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Still original order:", places)

places.reverse()
print("Reversed order:", places)

places.reverse()
print("Back to original order:", places)

places.sort()
print("Sorted permanently:", places)

places.sort(reverse=True)
print("Sorted permanently in reverse:", places)
