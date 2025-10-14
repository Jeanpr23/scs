# 07_06_three_exits.py

message = ""
while message != 'quit':
    message = input("Say something (type 'quit' to exit): ")
    if message != 'quit':
        print(message)

while True:
    message = input("Say something (type 'quit' to exit): ")
    if message == 'quit':
        break
    print(message)

active = True
while active:
    message = input("Say something (type 'quit' to exit): ")
    if message == 'quit':
        active = False
    else:
        print(message)
