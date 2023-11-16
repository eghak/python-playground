# here, we are importing the car_class module, so we can use the Car class to create object(s)
from car_class import Car

# create a new car object
car_1 = Car("Toyota", "Corolla", 2022, "White")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()