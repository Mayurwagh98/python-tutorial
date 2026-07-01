class Car():
    cars_created = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.cars_created += 1


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

Car("toyota","corolla")
Car("toyota","corolla")
ElectricCar("toyota","corolla","50kw")

print(Car.cars_created)