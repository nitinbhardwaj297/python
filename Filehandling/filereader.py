# import os
# file_path = input("enter the file path : ")

# if os.path.exists(file_path):
#     with open(file_path, 'r') as file:
#         file = file.read()
#         print(file)
# else:
#     print("file not found")


import os 
file_path = input("enter the file path: ")
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        print(file_content)
else:
    print("file not found")