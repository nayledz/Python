
class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.room_cost = 0
        self.appliances = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @property
    def monthly_cost(self):
        return self.__expenses + self.room_cost

    def calculate_expenses(self, *args):
        self.expenses = sum([el.get_monthly_expense() for arg in args for el in arg])
