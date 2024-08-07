# first ill check if file exists or not 
# then ill open it and find the string if exists or not 

import os 
count = 0
file_path = "file.txt"
if os.path.exists (file_path):
    with open("file_path", 'r') as file:
        for line in file:
            if line == "NitiN" :
                count+=1


    print("occurences of Nitin : ", count)
else:
    print("file not present ")



