unconfirmed_user = ["Alice","Susan",'Kamau',"JOHN"]

confirmed_user =[]

while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print(f"Verifying {current_user.title()}")
    confirmed_user.append(current_user)
    print(f"Successfully verified {current_user.title()}")