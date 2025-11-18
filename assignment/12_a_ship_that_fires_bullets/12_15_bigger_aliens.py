# 12_15_bigger_aliens.py

aliens = [
    {"size": "small", "points": 10},
    {"size": "medium", "points": 20},
    {"size": "big", "points": 30}
]

for alien in aliens:
    print(f"Alien size: {alien['size']}, points: {alien['points']}")