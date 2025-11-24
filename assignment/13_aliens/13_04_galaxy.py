# 13_04_galaxy.py

import random
import time

width = 40   
height = 20  
stars = 80   


galaxy = [[" " for _ in range(width)] for _ in range(height)]


for _ in range(stars):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    galaxy[y][x] = "*"


for row in galaxy:
    print("".join(row))
    time.sleep(0.05)