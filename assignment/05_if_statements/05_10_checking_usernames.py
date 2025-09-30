# 05_10_checking_usernames.py

current_users = ['jean', 'Dylan', 'David', 'admin']
new_users = ['jean', 'Raisa', 'David', 'admin']

for user in new_users:
    if user.lower() in [u.lower() for u in current_users]:
        print(f"Username '{user}' is already taken. Choose a different one.")
    else:
        print(f"Username '{user}' is available.")