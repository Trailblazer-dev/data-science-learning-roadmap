shoes = ["Nike", "Adidas", "Puma", "Reebok","New Balance","Converse"]

shoes.sort()
print(f"{shoes} in ascending order")
shoes.sort(reverse=True)
print(f"{shoes} in descending order")

print("\n\nTHE ABOVE SORTING IS USING SORT() WHICH PERMANENTLY CHANGES THE LIST\n")
print("THE BELOW SORTING IS USING SORTED() WITHOUT PERMANENTLY CHANGING THE LIST\n\n")
shoes2 = ["Nike", "Adidas", "Puma", "Reebok","New Balance","Converse"]
print(f"{shoes2} orginal list")
print(f"{sorted(shoes2)} in ascending order")
print(f"{sorted(shoes2, reverse=True)} in descending order")
print(f"{shoes2} orginal list")

cars = ["Toyota", "Honda", "BMW", "Mercedes", "Ford"]
cars.reverse()
print(f"{cars} in reverse order")