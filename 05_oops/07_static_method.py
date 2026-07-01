class Car():
    def __init__(self, brand):
        self.brand = brand

    @staticmethod
    def car_description():
        return 'this is car description'

car1 = Car("toyota")
print(car1.car_description())