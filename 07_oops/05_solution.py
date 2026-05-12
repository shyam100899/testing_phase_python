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
    def fuel_type(selef):
        return "diesel or petrol"

class EletricCar(Car):
    def __init__(self,brand,model,battery_size):
        self.battery_size = battery_size
        super().__init__(brand,model)
    def fuel_type(selef):
        return "electric charge"

my_car = Car("tata","safari")
print(my_car.model)
print(my_car.fuel_type())



electric_car = EletricCar("tesla","model s","85kwh")
print(electric_car.model)
print(electric_car.fuel_type())

