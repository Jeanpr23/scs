# 05_08_hello_admin.py

usernames = ['admin', 'jean', 'Dylan']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, welcome back!")