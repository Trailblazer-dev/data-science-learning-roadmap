# main file for the calculator project

from divide import divide
from multiple import multiply
from modolous import modulus

def add(a, b):
    """
    Returns the sum of a and b.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    result = a + b
def subtract(a, b):
    """
    Returns the difference of a and b.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The difference of a and b.
    """
    result = a - b
    return result

print("Welcome to the Calculator App!")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
choice = input("Enter choice (1/2/3/4/5): ")
if choice not in ['1', '2', '3', '4', '5']:
    print("Invalid choice. Please select a valid operation.")
    exit()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
elif choice == '5':
    print(f"{num1} % {num2} = {modulus(num1, num2)}")
else:
    print("Invalid choice. Please select a valid operation.")