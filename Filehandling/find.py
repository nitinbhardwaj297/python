import os

file_path = "/Users/apple/Documents/Python/day1.py"
search_string = "print"

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    count = file_content.count(search_string)

    if search_string in file_content:
        print("yes the string (print) is present")
        print(f"it is repeated {count} times in file ")
    else :
        print("no the search(print) is not present")
else:
    print("file path is not present")


