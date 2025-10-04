# 06_11_cities.py

cities = {
    'paris': {'country': 'france', 'population': '2.1 million'},
    'los angeles': {'country': 'usa', 'population': '3.9 million'},
    'miami': {'country': 'usa', 'population': '440,000'},
}

for city, info in cities.items():
    print(city.title(), "-", info)