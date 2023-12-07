import os 
file_path = "/Users/apple/Desktop/Nitin/Python/day9.py"

if os.path.exists(file_path):
    if os.path.isfile(file_path):
        print("this is a text file ")
    elif os.path.isdir(file_path):
        print("this is a directory ")
    else:
        print("this is neither a dir nor a file ")
else:
    print("the path dont exists ")