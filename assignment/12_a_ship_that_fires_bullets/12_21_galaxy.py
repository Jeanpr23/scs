# 12_21_galaxy.py


galaxy = []

import random
for i in range(5):
    star = {"x": random.randint(0, 800), "y": random.randint(0, 600)}
    galaxy.append(star)

print("Stars in the galaxy:")
for star in galaxy:
    print(star)