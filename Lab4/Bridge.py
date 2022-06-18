from abc import ABC, abstractmethod

class Engine():
    '''
    This represents the engine used by a vehicle.
    The engine has many characteristics, but the most important one is its type.
    An engine can be electric, hybrid, or combustion.
    '''
    def __init__(self, type, horsepower, weight):
        self.set_type(type)
        self.set_horsepower(horsepower)
        self.set_weight(weight)
    
    def display_details(self):
        print("This is an", self.type, "engine.")
        print("This engine has", self.hp, "horsepower and weights", self.weight, "kilos.")

    def set_type(self, type):
        self.type = type

    def set_horsepower(self, horsepower):
        self.hp = horsepower

    def set_weight(self, weight):
        self.weight = weight

class VehicleFactory(ABC, Engine):
    '''
    Abstract factory for vehicles.
    Each vehicle has a type for itself and its engine.
    Some additional details are its color and kilometers.
    '''
    @abstractmethod
    def __init__(self, engine):
        pass

    @abstractmethod
    def build_vehicle(self):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def set_kilometers(self, kilometers):
        pass


class Car(VehicleFactory):
    '''
    Extends the vehicle abstract factory in order to implement a car. 
    '''
    def __init__(self, engine, color, kilometers):
        self.set_engine(engine)
        self.set_color(color)
        self.set_kilometers(kilometers)

    def build_vehicle(self):
        print()
        print("A", self.color, "car has been built.")
        print("The car has", self.kilometers, "kilometers.")
        print("The engine's characteristics are:")
        self.engine.display_details()
        
    def set_color(self, color):
        self.color = color

    def set_engine(self, engine):
        self.engine = engine

    def set_kilometers(self, kilometers):
        self.kilometers = kilometers
    
class Motorcycle(VehicleFactory):
    '''
    Extends the vehicle abstract factory in order to implement a motorcycle. 
    '''
    def __init__(self, engine, color, kilometers):
        self.set_engine(engine)
        self.set_color(color)
        self.set_kilometers(kilometers)

    def build_vehicle(self):
        print()
        print("A", self.color, "motorcycle has been built.")
        print("The motorcycle has", self.kilometers, "kilometers.")
        print("The engine's characteristics are:")
        self.engine.display_details()
        
    def set_color(self, color):
        self.color = color

    def set_engine(self, engine):
        self.engine = engine

    def set_kilometers(self, kilometers):
        self.kilometers = kilometers

class Truck(VehicleFactory):
    '''
    Extends the vehicle abstract factory in order to implement a truck. 
    '''
    def __init__(self, engine, color, kilometers):
        self.set_engine(engine)
        self.set_color(color)
        self.set_kilometers(kilometers)

    def build_vehicle(self):
        print()
        print("A", self.color, "truck has been built.")
        print("The truck has", self.kilometers, "kilometers.")
        print("The engine's characteristics are:")
        self.engine.display_details()
        
    def set_color(self, color):
        self.color = color

    def set_engine(self, engine):
        self.engine = engine

    def set_kilometers(self, kilometers):
        self.kilometers = kilometers

# Testing the implementation.
new_engine = Engine('combustion', '197', '1200')
new_car = Car(new_engine, 'red', 0)
new_car.build_vehicle()

motorcycle_with_stolen_engine = Motorcycle(new_engine, 'green', '2614')
motorcycle_with_stolen_engine.build_vehicle()

new_truck_engine = Engine('electric', '2140', '3152')
heavy_truck = Truck(new_truck_engine, 'white', 142)
heavy_truck.build_vehicle()