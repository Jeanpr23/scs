# 08_12_sandwiches.py

def make_sandwich(*items):
    """Prints a summary of the sandwich being made."""
    print("Making a sandwich with:")
    for item in items:
        print(f"- {item}")

make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "avocado")
make_sandwich("peanut butter", "banana", "honey")