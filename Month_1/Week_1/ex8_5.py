def make_shirt(text='I Love Python',size="large"):
    print(f"You requested a shirt size {size} with this text {text}")
    
make_shirt("lg","Itachi")
make_shirt(size="extra large",text="Try It yourself")
print("-------------------------")
make_shirt()
make_shirt(size="medium")
make_shirt(text="Github my favorite social media ")


def describe_city(name,country='kenya'):
    print(f"{name} is in {country}")


describe_city("Nairobi")

describe_city(name="Kisumu")
describe_city(name="Moscow", country="Russia")