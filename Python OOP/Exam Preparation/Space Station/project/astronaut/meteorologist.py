from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_DECREASES_UNITS = 15

    def __init__(self, name: str):
        super().__init__(name, 90)