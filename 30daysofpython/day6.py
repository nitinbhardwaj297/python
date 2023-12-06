#tuples

fruit = ('fruits','banana','cake','coffee')
print(list(fruit))

#exercise 
tuple=()
brother= ('peter','nik','aman','sam')
sister= ('rochel','sany','nipi','anny')
sibling = brother+sister
print(sibling)

print(len(sibling))

#check item
tuple=('name','age','id','alcohol')
print('age' in tuple)

#accessing the index
print(tuple[1])

print(tuple[-1])

#slicing the tuples
print(tuple(1:4))

fruit=('cool','bol','nool','ool','boo')
del fruit