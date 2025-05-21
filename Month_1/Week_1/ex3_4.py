dinner_invite =["Njoroge","mani mani","Mum","Dad","Martha","Juma"]
print("The dinner invite list is:\n")

def dinner_invite_list(num):
    count = 0
    for invite in dinner_invite:
        count +=1
        print(f"I would like to invite you to dinner {invite.title()}")
        if count ==num:
            print(f"I am sorry, I can only invite {num} people to dinner.\n")
            break

dinner_invite_list(3)
cancelled_invite = dinner_invite.pop(0)
print(f"Mr {cancelled_invite.title()} can't make it to dinner")
dinner_invite.insert(0,"Juma")
print("The dinner invite list is:\n")
dinner_invite_list(3)

print("I have found a bigger dinner table so I can invite more people to dinner.\n")
print(f"how many people were in my list? {len(dinner_invite)}")
print("I will invite 2 more people to dinner.\n")

dinner_invite.insert(0,"Sister")
dinner_invite.append("Brother")
print("The dinner invite list is:\n")
dinner_invite_list(8)


print("\nI am sorry, I can only invite 2 people to dinner.\n")
while len(dinner_invite) >2:
    removed_invite = dinner_invite.pop()
    print(f"Sorry {removed_invite.title()}, I can't invite you to dinner.")
print("\nThe final dinner invite list is:\n")
dinner_invite_list(2)