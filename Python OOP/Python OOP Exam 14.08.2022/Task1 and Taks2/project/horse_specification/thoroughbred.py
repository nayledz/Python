from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    _MAX_SPEED = 140
    _SPEED_INCREASES_UNITS = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
