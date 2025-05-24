rivers ={
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississippi': 'usa',
}

for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.upper()}")
    
    
favorite_languages ={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

people ={'john','edward','phil','karen','isaac'}

for person in people:
    if person in favorite_languages.keys():
        print(f"thanks for taking the poll {person.title()}")
    else:
        print(f"{person.title()}, please take the poll")
print('------------------------------------')