# 09_15_lottery_analysis.py

import random

# Simulate multiple lottery draws
lottery_numbers = list(range(1, 51))
draws = 5  # number of times to draw

for i in range(draws):
    winning_numbers = random.sample(lottery_numbers, 6)
    print(f"Draw {i+1}: {winning_numbers}")