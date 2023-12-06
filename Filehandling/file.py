# import os

# # Create a directory
# directory_path = "/Users/apple/Documents/nitin"
# os.mkdir(directory_path)

# # Check if the directory was created successfully
# if os.path.exists(directory_path):
#     print("Directory is created successfully!")
# else:
#     print("It was not created successfully.")



import os
file_path="/Users/apple/Desktop/Nitin/Python/nitin.txt"
os.mkdir(file_path)
# create a directory
if os.path.exists(file_path):
    print("already present")
else:
    print("not present")
os.remove(file_path)
