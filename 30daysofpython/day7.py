#sets

set={}

fruits={'banana','orange','milk'}
#getting the set length

print(len(fruits))

print(fruits)

age={1,2,3,4}

print(2 in age)

name={'nitin','peter','sam','nik'}
name.add('belly')
print(name)


# update is use when we have to add more than one entity
car={'polo','virtus','lambo','urus'}
car.update(['audi','bmw'])
print(car)

#remove items from set
name={'nitin','nik'}
name.remove('nitin')
print(name)

# for clearing the set
name={'mits','nitin','ikks','drips'}
name.clear()
print(name)

fruits={'banana','orange','grapes','lemon'}
del fruits
# print(fruits)


#doing union of sets
fruits= {'banana','orange','grapes','lemon'}
name={'nitin','nik'}
set=fruits.union(name)
print(set)

fruits= {'banana','orange','grapes','lemon'}
name={'nitin','nik'}

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('twitter')
print(it_companies)
it_companies.update(['racloop','thales'])
print(it_companies)

(it_companies.remove('twitter'))
print(it_companies)
