def build_person(first_name,last_name,age=None):
    """Return a dictionary of information about a person"""
    person={'first_name':first_name,'last_name':last_name}
    if age:
        person['age']=age
    return person
musician =build_person("Kamau","Owino")
print (musician)