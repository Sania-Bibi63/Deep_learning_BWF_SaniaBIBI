class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        print("The car has started.")
        
    def stop(self):
        print("The car has stopped.")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        
    def charge(self):
        print("The car is charging.")
        
    def start(self):
        print("The electric car has started.")

my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
print(my_electric_car.make)            
print(my_electric_car.model)           
print(my_electric_car.year)           
print(my_electric_car.battery_capacity)  
my_electric_car.start()   
my_electric_car.stop()    
my_electric_car.charge()  
print("--------------------------")

# another example
# Define a superclass called Animal
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("The animal makes a sound.")

# Define a subclass called Dog, which inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="dog")
        self.breed = breed

    def make_sound(self):
        print("The dog barks.")

    def wag_tail(self):
        print("The dog wags its tail.")

# Create an instance 
my_animal = Animal("Mittens", "cat")
my_dog = Dog("Fido", "labrador")
my_animal.make_sound() 
my_dog.make_sound()     
my_dog.wag_tail()       
print(my_animal.name)