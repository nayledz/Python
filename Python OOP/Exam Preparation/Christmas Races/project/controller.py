
from project.race import Race
from project.driver import Driver
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        valid_types = ["MuscleCar", "SportsCar"]
        if car_type not in valid_types:
            return

        if self._find_car_same_model(model):
            raise Exception(f"Car {model} is already created!")

        car = ''
        if car_type == "MuscleCar":
            car = MuscleCar(model, speed_limit)
        elif car_type == "SportsCar":
            car = SportsCar(model, speed_limit)

        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)

        if self.__if_driver_exists(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = Race(race_name)

        if self.__if_race_exists(race_name):
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        valid_types = ["MuscleCar", "SportsCar"]
        driver = self._find_driver_by_name(driver_name)
        car = self._find_available_car(car_type)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car is None or car_type not in valid_types:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car
            old_model.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model.model} to {driver.car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {driver.car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self._find_driver_by_name(driver_name)
        if driver not in self.drivers:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._find_race_by_name(race_name)

        if race not in self.races:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_drivers = sorted([x for x in race.drivers], key=lambda x: x.car.speed_limit, reverse=True)[0:3]

        result = ''
        for driver in fastest_drivers:
            driver.add_win()
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}." + '\n'

        return result.strip()

    def _find_driver_by_name(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver
        return None

    def _find_car_same_model(self, model):
        for car in self.cars:
            if car.model == model:
                return True
        return False

    def _find_race_by_name(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return race
        return None

    def _find_available_car(self, car_type):
        for idx in range(len(self.cars) - 1, -1, -1):
            car = self.cars[idx]
            if car.car_type == car_type and not car.is_taken:
                return car
        return None

    def __if_driver_exists(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver
        return None

    def __if_race_exists(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return race
        return None