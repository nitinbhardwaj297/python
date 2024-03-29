print("hello world!")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
print(a)

print(a[1])

for x in a:
    print(x)

if "tempor" in a:
    print("yes it is there!")

##########################################################  Slicing   ######################################################################


b = "hello world!"
print(b[:5])

print(b[2:5])

# upper case
name = "Nitin Bhardwaj"
print(name.upper())

print(name.lower())


# strip the space #
introduction = " hell o my friend  s are u there "
print(introduction.strip())

# format the string #
age = 36
print(f"my age is {age}")

