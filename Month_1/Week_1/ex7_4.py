pizza_topping = "Enter a series of pizza toppings please"
pizza_topping += "\n enter 'quit' to exist or quit\n"

active =True

while active:
    prompt = input(pizza_topping)
    if prompt =='quit':
        active = False
    else:
        print(f"I will add {prompt} topping to your pizza")
        print("------------------------------------------")
        

switch = True

while switch:
    age = input("Please Enter Your age : \n enter 'quit' to exit\n\t")
    if age == 'quit':
        break
    age = int(age)
    if age <3:
        print("The Ticket is free")
    elif age >= 3 and age < 12 :
        print("The Ticket is $10")
    elif age>=12:
        print("The Ticket is $15")
    else:
        print("Invalid please try again")