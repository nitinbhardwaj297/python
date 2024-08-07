class person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        person.count += 1

    def printname(self):
        print("HI my name is ",self.name)

# creating the first object
person1 = person("John", "10")

person2 = person("Nitin", "10")