# chapter_2_examples.py

# Simple message with a variable
message = "Hello Python world!"
print(message)

# Changing the value of a variable
message = "Hello Python Crash Course world!"
print(message)

# Working with string methods
name = "Jean Paul"
print(name.title())   # Jean Paul Aponte Santiago
print(name.upper())   # JEAN PAUL APONTE SANTIAGO
print(name.lower())   # jean paul aponte santiago

# Combining strings
first_name = "JeanPaul"
last_name = "Aponte_Santiago"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
