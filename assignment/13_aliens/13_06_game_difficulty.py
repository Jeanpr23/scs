# 13_06_game_difficulty.py


import time
import random

print("Choose difficulty:")
print("1 = Easy")
print("2 = Medium")
print("3 = Hard")

choice = input("Enter 1, 2, or 3: ")


enemy_speed = 1.0       
enemy_spawn_rate = 0.10 
lives = 5

if choice == "1":
    enemy_speed = 1.2
    enemy_spawn_rate = 0.05
    lives = 7
elif choice == "2":
    enemy_speed = 1.0
    enemy_spawn_rate = 0.10
    lives = 5
elif choice == "3":
    enemy_speed = 0.6
    enemy_spawn_rate = 0.20
    lives = 3
else:
    print("Invalid choice, setting to Medium.")

print("\nGame starting...")
print(f"Lives: {lives}")
print(f"Enemy speed delay (lower = faster): {enemy_speed}")
print(f"Enemy spawn chance: {enemy_spawn_rate}\n")


for i in range(20):
    if random.random() < enemy_spawn_rate:
        print("ENEMY appeared!")
    else:
        print("...")

    time.sleep(enemy_speed)
