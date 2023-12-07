import os

file_directory = "/Users/apple/Documents/Python/remove.py"

os.remove(file_directoryls)


if os.path.exists(file_directory):
    print("file exists")
else: 
    print("file don't exists")