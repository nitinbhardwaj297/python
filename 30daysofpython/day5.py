# lists

emptylist=list()
print(len(emptylist))

# print list and its length  
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('fruits : ', fruits)
print('length of fruits : ', len(fruits))
print("vegetables : ", vegetables)
print("length of vegetables : ", len(vegetables))

#accessing items through lists

fruits = ['banana', 'orange', 'mango', 'lemon']        
print(fruits[0])
print(fruits[-1])

#slicing items

fruits = ['banana', 'orange', 'mango', 'lemon']                     

print(fruits[0:2])
print(fruits[:4])

fruits[0]='avocado'
print(fruits[0])

print('banana' in fruits)

#append

print(fruits.append('lime'))
    
#insert

print(fruits.append('lime'))

#remove

print(fruits.remove('mango'))

fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits.clear()
print(fruits)

#join with command

num1=[1,2,3,4]
num2=[5,6,7,8]

num1.extend(num2)
print(num1)

#reverse 
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

#sort
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)


print("age")
