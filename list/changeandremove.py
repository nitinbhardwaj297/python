fruits = ['mango', 'orange', 'banana', 'apple']
# change the 1 element of lists
fruits =  ['kiwi', 'orange', 'banana', 'apple']
print(fruits)

fruits[0] = 'mango'
print(fruits)

# insert items
fruits.insert(2,'watermelon')
print(fruits)

# we can also use append method / append add the element in the last of lists
fruits.append('guava')
print(fruits)

# to remove the element from the list we use this remove built in function
fruits.remove('guava')
print(fruits)