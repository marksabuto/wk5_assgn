class Vehicle:
    def move(self):
        print("The vehicle moves forward.")

class Car(Vehicle):
    def move(self):
        print("Driving on the highway 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the clouds ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the sea 🚤")

# Polymorphic behavior
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
