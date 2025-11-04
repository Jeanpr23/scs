# 09_13_ordered_dict_redux.py

from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jean'] = 'python'
favorite_languages['maria'] = 'java'
favorite_languages['david'] = 'c++'

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")