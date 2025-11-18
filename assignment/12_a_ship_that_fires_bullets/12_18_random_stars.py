# 12_18_random_stars.py

import random

for i in range(5): 
    spaces = " " * random.randint(0, 10)
    print(spaces + "*")