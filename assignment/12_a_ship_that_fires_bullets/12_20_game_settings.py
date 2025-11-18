# 12_20_game_settings.py
ary

game_settings = {
    "screen_width": 800,
    "screen_height": 600,
    "bg_color": "black",
    "ship_speed": 5
}

print("Game settings:")
for setting, value in game_settings.items():
    print(setting, ":", value)