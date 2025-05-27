def get_formatted_name(first_name,last_name):
    '''return a full name, neatly formatted'''
    full_name =f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Jimm', 'Karanja')
print (musician)


def get_formatted_names(first_name,last_name,middle_name=''):
    '''returns a full name ,neatly formatted.'''
    if middle_name:
        full_name =f"{first_name} {middle_name} {last_name}"
        
    else:
        full_name = f"{first_name} {last_name}"
    
    
    return full_name.title()

rapper = get_formatted_names('Wangeci',"street","queen")
banker = get_formatted_names(first_name="Elijah",middle_name="mukao",last_name='Mutiso')

print(f"{rapper} will now perform")
print(f"{banker} will talk about finance")

ropper = get_formatted_names("Ropert","Silent")
print(f"Fear {ropper}")