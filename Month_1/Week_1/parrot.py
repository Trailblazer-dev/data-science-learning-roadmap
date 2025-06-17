message = input("Tell me something, and I will repeat it back to you: ")
print (message)
name = input('Please enter your name: ')
print(f"Hello, {name.title()}! It's nice to meet you.")


prompt = "I have this friend of yours, but I don't know his name."
prompt += "\nWhat is his name? "
name = input(prompt)
print(f"Hello, {name.title()}! It's nice to meet you.")

age = input("How old are you? ")
age = int(age)
print(type(age),age)