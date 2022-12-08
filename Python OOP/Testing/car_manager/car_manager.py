class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed



import unittest
from unittest import TestCase


class CarTests(TestCase):
    MAKE = 'OPEL'
    MODEL = 'ASTRA'
    FUEL_CONSUMPTION = 10
    FUEL_CAPACITY = 40

    def setUp(self) -> None:
        self.car = Car('OPEL', 'ASTRA', 10, 40)

    def test_init(self):
        self.assertEqual(self.MAKE, self.car.make)
        self.assertEqual(self.MODEL, self.car.model)
        self.assertEqual(self.FUEL_CONSUMPTION, self.car.fuel_consumption)
        self.assertEqual(self.FUEL_CAPACITY, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_getters_and_setters(self):
        self.car.make = 'Audi'
        self.car.model = "A6"
        self.car.fuel_consumption = 15
        self.car.fuel_capacity = 50
        self.car.fuel_amount = 10

        self.assertEqual('Audi', self.car.make)
        self.assertEqual("A6", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(10, self.car.fuel_amount)







if __name__ == '__main__':
    unittest.main()