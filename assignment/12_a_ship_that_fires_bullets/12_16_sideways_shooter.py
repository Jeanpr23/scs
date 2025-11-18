# 12_16_sideways_shooter.py


shooter_x = 100

move_left = False
move_right = True  

if move_left:
    shooter_x -= 5
if move_right:
    shooter_x += 5

print("Shooter position:", shooter_x)