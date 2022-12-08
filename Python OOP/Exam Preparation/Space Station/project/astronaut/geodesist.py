from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN_DECREASES_UNITS = 10

    def __init__(self, name: str):
        super().__init__(name, 50)