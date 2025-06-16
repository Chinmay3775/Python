class Vehicle:
    def general_usage(self):
        print("General use : Transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm a Car")
        self.wheels=4
        self.has_roof=True
    
    def specific_usage(self):
        print("Specific Use: Commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm a MotorCycle")
        self.wheels=2
        self.has_roof=False

    def specific_uasage(self):
        print("Specific Usage: Road Trip , Racing ")

c= Car()
c.general_usage()
c.specific_usage()

m=MotorCycle()
m.general_usage()
m.specific_uasage()

print(isinstance(c,MotorCycle)) #false
print(issubclass(Car,Vehicle)) #true
