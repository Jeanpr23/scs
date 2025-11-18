# 12_12_shooting_aliens.py

aliens = [
    {"x": 100, "y": 50},
    {"x": 150, "y": 50},
    {"x": 200, "y": 50}
]
target_x = 150
target_y = 50

aliens = [alien for alien in aliens if not (alien["x"] == target_x and alien["y"] == target_y)]

print("Remaining aliens:")
for alien in aliens:
    print(alien)