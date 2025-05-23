for value in range(1,20):
    print(value)
    
million = list(range(1,1_000_000))
# print(million)
print(f"{min(million)} minimum value of million")
print(f"{max(million)} maximum value of million")
print(f"{sum(million)} sum of million")

odd_number = [value for value in range(1, 20) if value % 2 != 0]
print(odd_number)

threes = list(range(3,30,3))
print(threes)

cubes = [value**3 for value in range(1,10)]
for cube in cubes:
    print(cube)