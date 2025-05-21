friends = ["Alice","Smith","Rock","Brian","Clinton"]
for friend in friends:
    print(f"Hello {friend.title()}, How have you been?")


friends.append("Elijah")
print(friends)

laptops = ["Dell","HP","Lenovo","Asus"]
print(laptops)

laptops.insert(3,'china laptops')
print(laptops)
del laptops[3]
print(laptops)

poped_value = laptops.pop()
print(poped_value)

not_a_friend = friends.pop(2)
print(not_a_friend)
# when you want to delete an item from a list
# and not use that item in any way, use the del statement; if you want to use an
# item as you remove it, use the pop() method.

betrayer = "Brian"
friends.remove(betrayer)
print(friends)