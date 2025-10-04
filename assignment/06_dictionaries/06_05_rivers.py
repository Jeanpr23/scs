# 06_05_rivers.py

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")