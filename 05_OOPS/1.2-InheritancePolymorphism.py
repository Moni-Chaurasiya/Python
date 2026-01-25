# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class Vehical:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def move(self):
        print("Move!")

class Car(Vehical):
    pass

class Boat(Vehical):
    def move(self):
        print("Sail!")
        
class Plane(Vehical):
    def move(self):
        print("Fly!")
        
car1=Car("tesla","2")
boat1=Boat("Ibiza","10")
plane1=Plane("Boeing","727")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
        