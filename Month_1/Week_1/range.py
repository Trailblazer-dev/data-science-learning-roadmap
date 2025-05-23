distance =[]

for rang in range(0,500,50):
    distance.append(rang)
print (distance)

print(f"The minimum distance is {min(distance)}")
print(f"The maximum distance is {max(distance)}")
# a simpler way to do the above

temperature = list(range(30,40,2))
print(temperature)


squares =[value**2 for value in range(1,11)]
print(squares)