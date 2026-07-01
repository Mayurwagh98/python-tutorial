class Car:
    def __init__(self, brand):
        self.brand = brand

    @property
    def brand(self):
        return self._brand

car1 = Car("toyota")
car1.brand = "city"
print(car1.brand)
print(car1.car_brand)