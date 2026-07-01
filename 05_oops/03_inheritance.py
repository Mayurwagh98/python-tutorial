class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

car1 = ElectricCar("tesla","ES","56kW")
print(car1.brand)
print(car1.model)
print(car1.battery_size)
