# import os 
# file_path = "/Users/apple/Desktop/Nitin/Python/Loops/forloop.py"

# with open(file_path, 'r') as file:
#     content = file.read()
#     print(content)

def read(file_path):
    with open(file_path, 'r')as file:
        content = file.read()
        print(content)


read("/Users/apple/Desktop/Nitin/Python/Loops/forloop.py")



