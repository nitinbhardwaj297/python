class Dog:
    
    #class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"my name is {self.name} and age is {self.age} ")
dog1 = Dog("german", 10)
#print(dog1)
