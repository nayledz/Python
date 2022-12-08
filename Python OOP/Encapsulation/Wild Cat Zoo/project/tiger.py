from project.animal import Animal


class Tiger(Animal):
    MONEY_FOR_CARE = 45

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, self.MONEY_FOR_CARE)