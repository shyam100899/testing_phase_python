class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand= brand
        self.model= model
        Car.total_car += 1

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

Car("tata","safari")
Car("tata","nexon")
print(Car.total_car)




