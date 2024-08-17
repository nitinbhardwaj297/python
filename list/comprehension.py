"""List comprehension offers a shorter syntax when you want to create a new list based on the values 
of an existing list."""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]
print(new_list)

# join lists
list1 = [1,2,3,4,]
list2 = [1,2,5,6]
list_final = list1  + list2
print(list_final)

