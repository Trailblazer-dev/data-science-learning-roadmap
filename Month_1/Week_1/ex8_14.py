def sandwiches(*orders):
    """Prints the sandwich orders."""
    print("\nSandwich orders:")
    for order in orders:
        print(f"- {order}")

sandwiches('tuna', 'egg', 'chicken')
sandwiches('ham', 'cheese')
sandwiches('bacon')

def user_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile
user = user_profile('Kamau', 'Owino', location='Nairobi', field='Software Engineering')
print(user)

def car_info(manufacturer, model, **car_details):
    """Build a dictionary containing information about a car."""
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_details.items():
        car[key] = value
    return car
my_car = car_info('Toyota', 'Corolla', color='blue', year=2020, owner='Kamau')
print(my_car)