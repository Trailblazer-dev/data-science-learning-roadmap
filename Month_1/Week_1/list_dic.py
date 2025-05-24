alien_0={
    'color': 'green',
    'points': 5,
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}
alien_1 ={
    'color': 'red',
    'points': 10,
    'x_position': 0,
    'y_position': 15,
    'speed': 'fast'
}
alien_2 ={
    'color': 'yellow',
    'points': 15,
    'x_position': 0,
    'y_position': 5,
    'speed': 'slow'
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
for alien in aliens:
    for key, value in alien.items():
        print(key + ': ' + str(value))