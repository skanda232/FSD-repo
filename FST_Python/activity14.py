# class Car:
#     def __init__(self, manufacturer, model, make, transmission, color):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.make = make
#         self.transmission = transmission
#         self.color = color

#     def accelerate(self):
#         print(f"{self.manufacturer} {self.model} is moving")

#     def stop(self):
#         print(f"{self.manufacturer} {self.model} has stopped")


# # Creating 3 car objects
# car1 = Car("Toyota", "Corolla", 2022, "Automatic", "White")
# car2 = Car("Honda", "Civic", 2023, "Manual", "Black")
# car3 = Car("Tesla", "Model 3", 2024, "Automatic", "Red")

# # Using the methods
# car1.accelerate()
# car1.stop()

# car2.accelerate()
# car2.stop()

# car3.accelerate()
# car3.stop()

class Car:
    def __init__(self,manufacture,model,make,transmission,color):
        self.manufacture=manufacture
        self.model=model
        self.make=make  
        self.transmission=transmission
        self.color=color
    def accelerate(self):
        print(f"{self.manufacture} {self.model} is moving")
    def stop(self):
        print(f"{self.manufacture} {self.model} has stopped")
car1=Car("Toyota","Corolla",2022,"Automatic","White")
car2=Car("Honda","Civic",2023,"Manual","Black")
car3=Car("Tesla","Model 3",2024,"Automatic","Red")
car1.accelerate()
car1.stop()
car2.accelerate()
car2.stop()
car3.accelerate()
car3.stop()
