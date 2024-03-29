import os 
def addcontent(file_path):
    file = open(file_path, 'a')         #file handling adding content through append mode
    file.write("hello this is the additional content")
    file.close()

addcontent("/Users/apple/Desktop/Nitin/Python/Loops/forloop.py")


