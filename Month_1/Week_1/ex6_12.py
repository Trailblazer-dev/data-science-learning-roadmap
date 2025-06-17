person01={
    "name": "John Doe",
    "age": 30,
    "city": "New York",
}
person02={
    "name": "Jane Smith",
    "age": 25,
    "city": "Los Angeles",
}
person03={
    "name": "Bob Johnson",
    "age": 35,
    "city": "Chicago",
}
people =[person01, person02, person03]

for person in people:
    for value in person:
        print(f"{value}: {person[value]}")
    print('------------------------------------')
    
alice ={
    'kind':'cat',
    'owner':'Kevin',
    'age': 3,
    'color':'black',
}
bob ={
    'kind':'dog',
    'owner':'Kevin',
    'age': 5,
    'color':'brown',
}
candy ={
    'kind':'cat',
    'owner':'Lily',
    'age': 1,
    'color':'white',
}

pets =[alice, bob, candy]

for pet in pets:
    print(f"Pet owned by {pet['owner']}:")
    for value in pet:
        print(f"{value}: {pet[value]}")
    print('------------------------------------')
    
cities ={
    'nairobi':{
        'country':'Kenya',
        'population':2000000,
        'fact':'The capital city of Kenya',
    },
    'kisumu':{
        'country':'Kenya',
        'population':1000000,
        'fact':'The second largest city in Kenya',
    },
    'mombasa':{
        'country':'Kenya',
        'population':500000,
        'fact':'The third largest city in Kenya',
    },
    'Moscow':{
        'country':'Russia',
        'population':12000000,
        'fact':'The capital city of Russia',
    }
}

for city,info in cities.items():
    print(f"City: {city}")
    for value in info:
        print(f"\t{value}: {info[value]}")
    print('------------------------------------')
    

