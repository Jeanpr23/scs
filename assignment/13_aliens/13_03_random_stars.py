# 13_03_random_stars.py

import random

lines = 10  

for _ in range(lines):
    star_count = random.randint(1, 20)  
    print("*" * star_count)