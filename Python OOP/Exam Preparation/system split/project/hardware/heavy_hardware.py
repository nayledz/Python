import math

from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self,  name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value * 2

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = math.floor(0.75 * value)