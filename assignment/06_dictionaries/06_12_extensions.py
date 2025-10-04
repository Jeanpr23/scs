# 06_12_extensions.py


cities = {
    'paris': {'country': 'france', 'population': '2.1 million'},
    'los angeles': {'country': 'usa', 'population': '3.9 million'},
    'miami': {'country': 'usa', 'population': '440,000'},
    'san francisco': {'country': 'usa', 'population': '815,000'},
}

for city, info in cities.items():
    print(city.title(), "-", info)