# 12_10_aliens.py

aliens = []  

for i in range(3):
    alien = {"x": i * 50, "y": 100}
    aliens.append(alien)

print("Alien positions:")
for alien in aliens:
    print(alien)