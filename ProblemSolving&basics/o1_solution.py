class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model 

    def description(self):
        return f"This is a {self.brand} {self.model}."

car1 = Car("toyota", "hilux")
print(car1.brand, car1.model)

class Country(Car):
    def __init__(self, brand, model,name):
        super().__init__(brand, model)
        self.name = name 

    def description(self):
        return f"This is a {self.brand} {self.model} in {self.name}"

car2  = Country("bmw","x5", "India")
print(car2.brand, car2.model, car2.name)
print(car2.description())


