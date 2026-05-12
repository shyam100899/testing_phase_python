class Car:
    def __init__(self,brand,model):
        self.__brand= brand
        self.model= model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand+" !"
    
    def set_brand(self,brand):
         self.__brand = brand

class EletricCar(Car):
    def __init__(self,brand,model,battery_size):
        self.battery_size = battery_size
        super().__init__(brand,model)


my_car = Car("tata","safari")
print(my_car.model)
my_car.set_brand("mahindra")
print(my_car.get_brand())


electric_car = EletricCar("tesla","model s","85kwh")
print(electric_car.model)
print(electric_car.get_brand())

