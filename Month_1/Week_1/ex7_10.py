sandwich_orders =['chicken','pastrami','beef','pastrami','pork','mutton','pastrami']
finished_sandwiches =[]


print("Delihas run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)
    
print(finished_sandwiches)




active = True
responses ={}
while active:
    name =input("Enter your name please\n")
    vacation = input(f"{name} if you could visit one place in the world, wherewould you go?\n")
    responses[name]=vacation
    
    
    exit = input("if you would not like to repeat enter 'exit'")
    if exit =='exit':
        active = False
    