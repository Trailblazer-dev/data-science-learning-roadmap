users = ["admin","lecturer","student","staff","dean","vice chancellor"]

if not users:
    print("We need to find some users!")

for user in  users:
    if( user.lower() == "admin"):
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
        
current_users =["qwen","john","jane","johnson","peter"]
new_users = ["Qwen","Janet","Peter","Juma","Martha"]

current_users_lower = [user.lower() for user in current_users]
print(current_users_lower)


for new_user in new_users:
    if(new_user.lower() in current_users):
        print(f"Sorry {new_user.title()}, that name is taken.")
    else:
        print(f"Welcome {new_user.title()}, that name is available.")
        
positions =[1,2,3,4,5,6,7,8,9]

for position in positions:
    if(position == 1):
        print(f"{position}st \n")
    elif(position == 2):
        print(f"{position}nd \n")
    elif(position == 3):
        print(f"{position}rd \n")
    else:
        print(f"{position}th \n")
