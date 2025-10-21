# 8_11_unchanged_magician

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    new_list = []
    for name in names:
        new_list.append(name + " the Great")
    return new_list

magicians = ["Houdini", "Blaine", "Angel"]
great_magicians = make_great(magicians[:])

show_magicians(magicians)
print("---")
show_magicians(great_magicians)