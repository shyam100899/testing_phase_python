# Create a car class with attribute like brand and model.then create the instance of the class.

'''

Class should be capitalized.

'''

class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

my_car = Car("tata","safari")
print(my_car.brand)
print(my_car.model)



