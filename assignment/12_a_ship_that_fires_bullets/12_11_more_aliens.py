# 12_11_more_aliens.py

aliens = []
rows = 2
columns = 3

for row in range(rows):
    for col in range(columns):
        alien = {"x": col * 50, "y": row * 50}
        aliens.append(alien)

print("Aliens positions:")
for alien in aliens:
    print(alien)