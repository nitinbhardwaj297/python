# functions
def name():
    print('nitin')

name()

# without parameters
def generatename():
    firstname='nitin'
    lastname='bhardwaj'
    space=' '
    fullname=firstname+space+lastname
    print(fullname)

generatename()

def numbers():
    num1=22
    num2=44
    add=num1+num2
    print(add)

numbers()

def nitin():
    num=2
    mun=3
    total=num+mun
    return total
print(nitin())

# 2 parameters

def names(naam, last):
    fullname= naam+" "+last
    return fullname
print(names('nitin','bhardwaj'))

def range(para1 , para2):
    print(para1)
    print(para2)
    total=para1+para2
print(range(para1="hello", para2="world"))


 