#dictionary


#empty dictionary
empty_dict={}

person = {
    'first_name':'nitin',
    'last_name':'bhardwaj',
    'age':250,
    'country':'india',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person)

print(len(person))

#accessing dictionary items

print(person['first_name'])
print(person['address'])
print(person['age'])

#modify items in a dictionary
person['first_name'] = 'nittsss'
person['age'] = 20

print(person)

person['job_title'] = 'devops engineer'
person['skills'].append('html')
print(person)

print(person.clear())

#exercise

dog={}
dog['name']='bruno'
dog['breed']='labra'

print(dog)
student = {
    'first_name':'nitin',
    'last_name':'bhardwaj',
    'age':250,
    'country':'india',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(len(student))
del student
print(student)