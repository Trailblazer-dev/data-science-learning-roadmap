current_number =1

while current_number <5:
    print(current_number)
    current_number +=1



message = "Tell me something and I will repeat it back to you"
message +="\n Enter 'quit' to end the program\n"
prompt=""

while prompt !='quit':
    prompt = input(message)
    if prompt =='quit':
        print("quiting")
        break
    
    
count = 0

while count < 10:
    count +=1
    if count % 2 == 0:
        continue
    print(count)
    