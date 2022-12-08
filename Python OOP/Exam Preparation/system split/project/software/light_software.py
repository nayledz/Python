import math
from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, 'Light', capacity_consumption, memory_consumption)

    @property
    def capacity_consumption(self):
        return self.__capacity_consumption

    @capacity_consumption.setter
    def capacity_consumption(self, value):
        self.__capacity_consumption = math.floor(value + (0.5 * value))

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        self.__memory_consumption = math.floor(value - (0.5 * value))