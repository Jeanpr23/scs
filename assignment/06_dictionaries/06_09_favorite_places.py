# 06_09_favorite_places.py

favorite_places = {
    'jeanpaul': ['California los angeles', 'Paris', 'Florida'],
    'Dylan': ['london', 'rome'],
    'Daved': ['gotham', 'new york'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(" -", place.title())