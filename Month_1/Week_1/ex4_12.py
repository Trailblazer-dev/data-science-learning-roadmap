djs=["Moon","Grauchi","alekie","festa","tophaz"]
print("The fists three djs are :",djs[0:3])
print(f"length is {len(djs)}")
print("middle djs are :",djs[2:4])
print("last djs are :",djs[-3:])


pizza = ["pepperoni","mushroom","cheese","veggie"]
friends_pizzas = pizza[:]
pizza.append("chicken")
friends_pizzas.append("pineapple")
print("My favorite pizzas are:")
for pizza in pizza: 
    print("I like",pizza,"pizza")
    
print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas: 
    print("I like",pizza,"pizza")