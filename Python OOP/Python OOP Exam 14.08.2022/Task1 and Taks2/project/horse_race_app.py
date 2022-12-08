from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_types = ["Appaloosa", "Thoroughbred"]
        if horse_type not in valid_types:
            return

        if self.__is_found_horse_with_the_same_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = ''
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__is_found_jockey_with_the_same_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__is_found_race_with_the_same_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        valid_types = ["Appaloosa", "Thoroughbred"]
        jockey = self.__find_jockey_by_name(jockey_name)
        horse = self._find_available_horse(horse_type)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if horse is None or horse_type not in valid_types:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {jockey.horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if not self.__is_found_race_with_the_same_type(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__find_jockey_by_name(jockey_name)
        race = self.__find_race_by_type(race_type)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if not self.__is_found_race_with_the_same_type(race_type):
            raise Exception(f"Race {race_type} could not be found!")
        race = self.__find_race_by_type(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted([x for x in race.jockeys], key=lambda x: x.horse.speed, reverse=True)[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def __is_found_horse_with_the_same_name(self, name):
        for horse in self.horses:
            if horse.name == name:
                return True
        return False

    def __is_found_jockey_with_the_same_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return True
        return False

    def __is_found_race_with_the_same_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return True
        return False

    def _find_available_horse(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[idx]
            if horse.horse_type == horse_type and not horse.is_taken:
                return horse
        return None

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None