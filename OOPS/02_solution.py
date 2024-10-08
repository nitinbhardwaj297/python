class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar:
    def __init__(self, brand, model, battery_size):
        super.__init__(brand,model)
        self.battery_size = battery_size


tesla_car = ElectricCar("tesla","s",'85kwh')
print(tesla_car.full_name())

car1 = Car('toyota', 'corolla')
print(car1.full_name())
print(car1.brand)
print(car1.model)
