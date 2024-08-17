import os 
file_path = "/Users/apple/Desktop/Nitin/Python/nitin.py"

if os.path.exists(file_path):
    print('file exists')
else:
    print("file don't exists")