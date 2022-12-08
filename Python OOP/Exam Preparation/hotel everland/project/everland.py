from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if not any(r.family_name == room.family_name for r in self.rooms):
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumption = sum([room.monthly_cost for room in self.rooms])
        return f"Monthly consumption: {monthly_consumption:.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            if room.budget < room.monthly_cost:
                self.rooms.remove(room)
                result += f"{room.family_name} does not have enough budget and must leave the hotel." + '\n'
            room.budget -= room.monthly_cost
            result += f"{room.family_name} paid {room.monthly_cost:.2f}$ and have {room.budget:.2f}$ left." + '\n'
        return result.strip()

    def status(self):
        result = f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. ' \
                    f'Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$' + '\n'

        for r in self.rooms:
            if r.children:
                for i, child in enumerate(r.children):
                    result += f"--- Child {i + 1} monthly cost: {child.get_monthly_expense():.2f}$" + '\n'

        for r in self.rooms:
            if r.appliances:
                result += f"--- Appliances monthly cost: {r.calculate_expenses(r.appliances):.2f}$" + '\n'

        return result.strip()