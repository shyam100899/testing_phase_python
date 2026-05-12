class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand= brand
        self.__model= model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand+" !"
    
    def set_brand(self,brand):
         self.__brand = brand
    def fuel_type(self):
        return "diesel or petrol"
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    @property
    def model(self):
        return self.__model
    
class EletricCar(Car):
    def __init__(self,brand,model,battery_size):
        self.battery_size = battery_size
        super().__init__(brand,model)
    def fuel_type(self):
        return "electric charge"

my_car = Car("tata","safari")
#my_car.model="city"
your_car = Car("tata","nexon")

#print(my_car.model)
print(my_car.model)
print(my_car.general_description()) # not good practice
print(Car.general_description())





