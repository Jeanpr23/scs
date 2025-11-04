# 11_02_population.py

def city_country(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()} - Population: {population}"
    else:
        return f"{city.title()}, {country.title()}"

print(city_country("paris", "france", 2141000))
print(city_country("tokyo", "japan", 13929000))
print(city_country("sydney", "australia"))
