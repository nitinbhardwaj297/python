import os
file="/Users/apple/Desktop/Nitin/Python/day18.py"
directory = file
if os.path.exists(directory):
    print("directory exists!")

else:
    print("directory dont exists!")
