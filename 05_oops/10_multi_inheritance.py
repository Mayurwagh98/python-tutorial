class Battery():
    def battery_info(self):
        return "this is battery"

class Engine():
    def engine_info(self):
        return "this is engine"

class ElectricCar(Battery, Engine):
    pass

car1 = ElectricCar()
print(car1.battery_info())
print(car1.engine_info())