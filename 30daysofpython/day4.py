#all operations on strings

# single line comment 
letter = 'n'
print(letter)
#pirnt length of string
print(len(letter)) 

sentence="this is the 4th day of python"
print(sentence)

#multiline string
multiline_string='''hey! everyone how u all are doing
i hope this weekend is good for you .'''
print(multiline_string)
#another way of writing the string
multiline_string=""" hey! everyone how u all are doing
i hope this weekend is good for you. """
print(multiline_string)

#string concatenation
firstname='nitin'
lastname='bhardwaj'
space=' '
fullname= firstname+space+lastname
print(fullname)
print(len(firstname) > len(lastname))

#accessing characters in strings by index
fullname='nitin'
print(fullname[0])
print(fullname[1])
print(fullname[2])
print(fullname[3])

#for accessing variable from right side
fullname='nitin'
print(fullname[-1])
print(fullname[-2])

#slicing 
language='python'
print(language[1:4])
print(language[:4])
print(language[1:2])
print(language[1:])

#escape sequence
print('day4\t2\t4')
print('i hope every one enjoying the python challenge. \n do you?')

# string methods
challenge='he he he he ' #capitalize the first word
print(challenge.capitalize())

print(challenge.count('h')) #count the word

number='10'
print(number.isnumeric())

challenge='30 days of python'
print(challenge.replace('python', 'coding'))

#if string split from left
challenge = '30 days of python'
print(challenge.split())

challenge='python is soo cool'
print(challenge.startswith('python'))

challenge='30 days of python is awesome'
print(challenge.swapcase())


