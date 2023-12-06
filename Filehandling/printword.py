import os
file_path = "/Users/apple/Documents/Python/day1.py"


if os.file.exists(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

        