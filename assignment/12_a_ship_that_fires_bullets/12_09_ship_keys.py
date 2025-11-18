# 12_09_ship_keys.py


ship_x = 100
ship_y = 300

press_left = False
press_right = True  


if press_left:
    ship_x -= 5
if press_right:
    ship_x += 5

print("Ship position:", ship_x, ship_y)