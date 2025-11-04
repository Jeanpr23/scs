# 09_14_lottery.py

import random

# Simulate a lottery with numbers from 1 to 50
lottery_numbers = list(range(1, 51))
winning_numbers = random.sample(lottery_numbers, 6)

print("Winning lottery numbers are:", winning_numbers)