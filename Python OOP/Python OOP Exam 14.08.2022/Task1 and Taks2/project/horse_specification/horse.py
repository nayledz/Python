from abc import ABC, abstractmethod


class Horse(ABC):
    _MAX_SPEED = 0
    _SPEED_INCREASES_UNITS = 0

    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.__class__._MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        increased_speed = self.speed + self._SPEED_INCREASES_UNITS
        self.speed = min(self._MAX_SPEED, increased_speed)

    @property
    def horse_type(self):
        return self.__class__.__name__
