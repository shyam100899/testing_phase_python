
class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand= brand
        self.__model= model
        Car.total_car += 1

class Battery:
    def batetry_info(self):
        return "this is baterry"
class Engine:
    def engine_info(self):
        return "this is engine"
class Eletrcicar2(Battery,Engine,Car):
    pass

my_new_tesla = Eletrcicar2("tesla","model s")
print(my_new_tesla.batetry_info())
print(my_new_tesla.engine_info())