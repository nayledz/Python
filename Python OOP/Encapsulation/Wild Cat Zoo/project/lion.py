from project.animal import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, self.MONEY_FOR_CARE)