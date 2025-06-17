alien_color = "red"
if(alien_color == "green"):
    print("You have just earned 5 points")
elif(alien_color == 'yellow'):
    print("You have have been deducted 5 points")
else:
    print("You have just earned 10 points")



age = 14
if( age < 2):
    print("Your are a baby")
elif(age >= 2 and age < 4):
    print("You are a toddler")
elif(age >= 4 and age < 13):
    print("You are a kid")
elif(age >= 13 and age < 20):
    print("You are a teenager")
elif(age >= 65):
    print("You are an elder")
else:
    print("You are an adult")
    
friuits = ["banana","apple","orange"]
if("banana" in friuits):
    print("You have a banana")
if("apple" in friuits):
    print("You have a apple")
if("orange" in friuits):
    print("You have a orange")
if("mango" in friuits):
    print("You have a mango")