while loops

count = 0
while(count<5):
    print(count)
    count=count+1
else:
    print("count")

another example

name =0
while(name<5):
    if name==3:
        continue
    print(name)
    name=name+1


for loop

numbers=(1,2,3,4)
for number in numbers:
    print(number)

for loop with string

language="python"
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

cool = [1,2,3,4]
for i in cool:
    print(cool)

person = {
    'first_name':'Nitin',
    'last_name':'Bhardwaj',
    'age':2,
    'country':'Finland',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)
nitin =(1,2,3,4)
for i in nitin:
    if nitin == 3:
        continue
    print("next number should be ", nitin+1)
    if(nitin !=5):
        print("printing else")
    else:
        print("loop's end")

# nested loop 

book=(1,2,3,4,5)
for i in  book :
    print("numbers are in book")
    if(i == 6):
        print("number are out of bound")
    else:
        print("ok")


# exercise 1 
for i in range(0, 5):
    print(i)

def dhruv():
    print('hello')

dhruv()
