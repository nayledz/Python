import math

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self,  name: str, capacity: int, memory: int):
        super().__init__(name, "Power", capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = math.floor(value * 0.25)

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = math.floor(value + (0.75 * value))