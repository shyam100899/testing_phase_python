class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model
    def full_name(self):
        return f"{self.brand} {self.model}"

class EletricCar(Car):
    def __init__(self,brand,model,battery_size):
        self.battery_size = battery_size
        super().__init__(brand,model)


electric_car = EletricCar("tesla","model s","85kwh")
print(electric_car.model)
print(electric_car.brand)
print(electric_car.full_name())
