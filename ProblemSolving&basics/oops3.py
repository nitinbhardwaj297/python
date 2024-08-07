# this is the parent class

class Dog:

    def __init__(self, name , age):
        self.name = name
        self.age__ = age
 
    # creating the other method 
    def bark(self):
        print("bark, bark") 

    def dog_info(self):
        print(self.name + " is " + str(self.age) + " years old .")

    # getter methods to access attributes

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age 
    
    # setter methods to modify attributes 
    def set_name(self, name):
        self._name = name
    
    def set_age(self,age):
        self._age = age

 
    


dog1= Dog("BROWN", 18) # creating the object 
dog1.show()
print(dog1.name, dog1.age) # to print the object attributes




# creating the child classx


dog1.bark()

dog1.dog_info()


