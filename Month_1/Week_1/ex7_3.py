rental_car = input("What kind of rental car would you like? ")

print(f"Let me see if I can find you a {rental_car.title()}.")

seats = input("HOw many people are in your dinner group? ")
seats = int(seats)
if( seats>8):
    print("Please wait for a table")
else:
    print("Your table is ready")
    
number = input("Enter a number and I will tell you if it is a multiple of 10 .")
number = int(number)

if number % 10 == 0 :
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")