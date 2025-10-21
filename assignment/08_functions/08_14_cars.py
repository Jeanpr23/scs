# 08_14_cars.py

def make_car(manufacturer, model, **features):
    """Builds a dictionary with car information."""
    car = {
        "manufacturer": manufacturer,
        "model": model
    }
    car.update(features)
    return car

my_car = make_car("Subaru", "Outback", color="blue", tow_package=True)

print(my_car)