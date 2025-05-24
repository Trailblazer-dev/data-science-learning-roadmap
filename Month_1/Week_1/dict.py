alien_o={'color':'green','points':5}
print(alien_o['color']+" ",alien_o['points'])

alien_o['x_position']=0
alien_o['y_position']=25
print(alien_o)
alien_o['speed']='medium'

if alien_o['speed'] == 'slow':
    alien_o['x_position'] +=1
elif alien_o['speed'] == 'fast':
    alien_o['x_position'] +=4
else:
    alien_o['x_position'] +=2
    

print(alien_o['x_position'])
print(alien_o)
del alien_o['speed']
print("after del",alien_o)




alien_1={}
alien_1['color']='red'
alien_1['points']=10
print(alien_1)
alien_1['color']='yellow'
print(alien_1)


# laptops_rating ={}

# laptops_rating['model']="hp"
# laptops_rating = {
#     {
#     'model':'hp',
#     'rating':4.8,
#     },{
#     'model':'dell',
#     'rating':4.5,
#     }
# }
# print(laptops_rating)