# 06_06_polling.py

favorite_languages = {
    'jean': 'python',
    'Dylan': 'c',

}

people = ['jean', 'Dylan']

for person in people:
    if person in favorite_languages:
        print("Thank you,", person.title())
    else:
        print(person.title(), "please take the poll.")
