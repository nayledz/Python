from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
        new_aquarium = ''
        if aquarium_type not in valid_types:
            return "Invalid aquarium type."

        if aquarium_type == 'FreshwaterAquarium':
            new_aquarium = FreshwaterAquarium(aquarium_name)

        elif aquarium_type == 'SaltwaterAquarium':
            new_aquarium = SaltwaterAquarium(aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        valid_types = ["Ornament", "Plant"]
        new_decoration = ''
        if decoration_type not in valid_types:
            return "Invalid decoration type."

        if decoration_type == 'Ornament':
            new_decoration = Ornament()

        elif decoration_type == 'Plant':
            new_decoration = Plant()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        new_decoration = self._find_decoration(decoration_type)
        new_aquarium = self._find_aquarium(aquarium_name)
        if new_decoration is None:
            return f"There isn't a decoration of type {decoration_type}."
        if new_aquarium is None:
            return
        new_aquarium.add_decoration(new_decoration)
        self.decorations_repository.remove(new_decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_types = ["FreshwaterFish", "SaltwaterFish"]
        new_fish = ''
        if fish_type not in valid_types:
            return f"There isn't a fish of type {fish_type}."

        if fish_type == 'FreshwaterFish':
            new_fish = FreshwaterFish(fish_name, fish_species, price)

        elif fish_type == 'SaltwaterFish':
            new_fish = SaltwaterFish(fish_name, fish_species, price)

        aquarium = self._find_aquarium(aquarium_name)
        return aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self._find_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self._find_aquarium(aquarium_name)
        value = sum([fish.price for fish in aquarium.fish]) + sum([d.price for d in aquarium.decorations])
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'
        return result.strip()

    def _find_decoration(self, decoration_type):
        for decoration in self.decorations_repository.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration

    def _find_aquarium(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium


