from abc import ABC, abstractmethod

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        sum = 0
        for decoration in self.decorations:
            sum += decoration.comfort
        return sum

    def add_fish(self, fish: BaseFish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        if self.fish_type != fish.__class__.__name__:
            return "Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):

        result = f"{self.name}:" + '\n' + "Fish: "
        if self.fish:
            result += ' '.join([f.name for f in self.fish]) + '\n'
        else:
            result += "none" + '\n'

        result += f"Decorations: {len(self.decorations)}" + '\n'
        result += f"Comfort: {self.calculate_comfort()}"

        return result.strip()

    @property
    @abstractmethod
    def fish_type(self):
        pass



