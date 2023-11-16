# Create an empty dictionary called dog
dog={}
# Add name, color, breed, legs, age to the dog dictionary
dog={
    'name':'Bonny',
    'color':'white',
    'breed':'hucky',
    'legs': 4 ,
    'age': 9
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'first_name': 'Ben',
    'last_name':'Martin',
    'gender':'men',
    'age': 45,
    'marital_status':'is_married',
    'skills':['skiing','bull_riding','swimming'],
    'country':'Thailand',
    'city':'Cavanula',
    'addres':{
        'street':'Haska',
        'flat_number':34
    }
}

# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student['skills'])
# Modify the skills values by adding one or two skills
print(student['skills'].append('drawing'))
# Get the dictionary keys as a list
keys=student.keys()
print(student)
# Get the dictionary values as a list
values=student.values()
print(values)
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
print(student.pop('swimming'))
# Delete one of the dictionaries
del student ['last_name']
