from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        valid_types = ["Biologist", "Geodesist", "Meteorologist"]

        if astronaut_type not in valid_types:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = ''
        if astronaut_type == Biologist.__name__:
            astronaut = Biologist(name)
        elif astronaut_type == Geodesist.__name__:
            astronaut = Geodesist(name)
        elif astronaut_type == Meteorologist.__name__:
            astronaut = Meteorologist(name)

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        self.planet_repository.add(planet)
        planet.items = items.split(', ')
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        number_of_astronauts = 0

        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts_oxygen_over_30 = sorted([x for x in self.astronaut_repository.astronauts if x.oxygen > 30], key=lambda x: x.oxygen, reverse=True)[0:5]

        if len(astronauts_oxygen_over_30) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        for astronaut in astronauts_oxygen_over_30:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            number_of_astronauts += 1

        if len(planet.items) == 0:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {number_of_astronauts} astronauts participated in collecting items."
        else:
            self.unsuccessful_missions += 1
            return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!" + \
                 '\n' + f"{self.unsuccessful_missions} missions were not completed!" + '\n' \
                 + "Astronauts' info:" + '\n'

        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}" + '\n'
            result += f"Oxygen: {astronaut.oxygen}" + '\n'
            result += f"Backpack items: {', '.join(astronaut.backpack) if len(astronaut.backpack) > 0 else 'none'}"

        return result.strip()



