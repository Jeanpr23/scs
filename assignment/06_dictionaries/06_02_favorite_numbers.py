# 06_02_favorite_numbers.py

favorite_numbers = {
    'Jean Paul': [21, 7],
    'Dylan': [40, 99],
    'David': [3, 14, 27],
    'Raisa': [8],
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")