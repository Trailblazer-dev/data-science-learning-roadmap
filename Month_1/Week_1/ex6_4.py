person ={
    'first_name':'Kevin',
    'last_name':'Chen',
    'city':'Tainan'
}
for p in person:
    print(p, ':', person[p])
print('------------------------------------')


favorite_numbers ={
    'alice': 7,
    'bob': 42,
    'charlie': 3,
    'dave': 8,
    'eve': 13
}
print(favorite_numbers['alice'])
print(favorite_numbers['bob'])
print(favorite_numbers['charlie'])
print(favorite_numbers['dave'])
print(favorite_numbers['eve'])
print('------------------------------------')

for key,value in favorite_numbers.items():
    print(key, ':', value)
print('------------------------------------')


for key in favorite_numbers.keys():
    print(key)
print('------------------------------------')

for key in sorted(favorite_numbers.keys()):
    print(key)
print('------------------------------------')
favorite_numbers['fred']=7
print(favorite_numbers)
print('values------------------------------------')
for value in favorite_numbers.values():
    print(value)
    
print('------------------------------------')
# use set to remove duplicates
for value in set(favorite_numbers.values()):
    print(value)
print('------------------------------------')

for value in sorted(set(favorite_numbers.values())):
    print(value)
print('------------------------------------')