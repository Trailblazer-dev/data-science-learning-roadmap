number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)

if(number % 2 ==0 ):
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")