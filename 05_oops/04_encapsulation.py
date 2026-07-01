class Car():
    def __init__(self, brand, model):
        self.__brand = brand #private attribute
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand

car1 = Car("Toyota",'corolla')

# print(car1.brand) Not accessible since its a private attribute
print(car1.get_brand())
print(car1.model)
