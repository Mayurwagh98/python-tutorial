class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def fule_type():
        return "petrol or diesel"

class ElectricCar():
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fule_type():
        return "Electric"

print(Car.fule_type())
print(ElectricCar.fule_type())