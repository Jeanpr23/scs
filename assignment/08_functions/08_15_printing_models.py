# 08_15_printing_models.py

def print_models(unprinted, completed):
    """Simulates printing each design and moves it to completed."""
    while unprinted:
        current = unprinted.pop()
        print(f"Printing model: {current}")
        completed.append(current)

def show_completed_models(completed):
    """Displays all completed models."""
    print("Completed models:")
    for model in completed:
        print(f"- {model}")

# Lists of designs
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)