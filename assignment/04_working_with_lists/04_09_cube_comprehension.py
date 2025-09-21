# 04_09_cube_comprehension.py
# list comprehension to generate cubes of numbers from 1 to 10

cubes = [number ** 3 for number in range(1, 11)]

# Print each cube
for cube in cubes:
    print(cube)