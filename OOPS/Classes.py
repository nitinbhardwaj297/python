""" this is the classes in python which use to structre the code """
" this is library management system "

# this is the book class
class Book:
    def __init__(self,Title, author):
        self.Title = Title
        self.author = author

    
#this is the member class
class Member:
    def __init__(self, Name, member_id):
        self.Name = Name
        self.member_id = member_id


# this is the library class
class Library:
    def __init__(self):
        self.Book = Book
        self.Member = Member


Book1 = Book("the story of why", "Darwin")
Book2 = Book("the hype", "cool fred")

Member1 = Member("Nitin","1")

Library = Library()     


 

  