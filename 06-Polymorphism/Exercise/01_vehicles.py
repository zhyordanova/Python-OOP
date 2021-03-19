from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def get_fuel_needed(self, distance, air_condition_consumption):
        return (self.fuel_consumption + air_condition_consumption) * distance


class Car(Vehicle):
    _FUEL_CONSUMPTION_INCREASED = 0.9

    def drive(self, distance):
        fuel_needed = self.get_fuel_needed(distance, Car._FUEL_CONSUMPTION_INCREASED)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle, ABC):
    _FUEL_CONSUMPTION_INCREASED = 1.6
    _KEPT_FUEL_PERCENTAGE = 0.95

    def drive(self, distance):
        fuel_needed = self.get_fuel_needed(distance, Truck._FUEL_CONSUMPTION_INCREASED)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck._KEPT_FUEL_PERCENTAGE


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

