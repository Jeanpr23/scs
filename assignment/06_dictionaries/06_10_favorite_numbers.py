# 06_10_favorite_numbers.py

favorite_numbers = {
    'jean': [21, 7],
    'Zelda': [5, 9],
    'Steve': [17, 99],
}

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:", numbers)