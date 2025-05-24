users ={
    'john':{
        'first':'John',
        'last':'Doe',
        'location':'New York'
    },
    'jane':{
        'first':'Jane',
        'last':'Doe',
        'location':'New York'
    },
    'james':{
        'first':'James',
        'last':'Doe',
        'location':'New York'
    },
    'jill':{
        'first':'Jill',
        'last':'Doe',
        'location':'New York'
    },
    'jack':{
        'first':'Jack',
        'last':'Doe',
        'location':'New York'
    },
}

for user in users:
    print(user)
    print(f"For {user} his user infomation is :")
    for user_info in users[user]:
        print(user_info)
        for value in users[user][user_info]:
            print(f"{value}")
            
            
# alternative option for printing the dictionary
for user, user_info in users.items():
    print(user)
    print(f"For {user} his user infomation is :")
    for key, value in user_info.items():
        print(f"{key}: {value}")