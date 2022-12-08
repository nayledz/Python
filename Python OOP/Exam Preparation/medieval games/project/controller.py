class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type != "Food" and sustenance_type != "Drink":
            return
        supply, index = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        player.stamina = min(supply.energy + player.stamina, 100)

        self.supplies.pop(index)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):

        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        not_enough_stamina = ''
        if first_player and first_player.stamina == 0:
            not_enough_stamina += f"Player {first_player_name} does not have enough stamina.\n"

        if second_player and second_player.stamina == 0:
            not_enough_stamina += f"Player {second_player_name} does not have enough stamina.\n"
        if not_enough_stamina != '':
            return not_enough_stamina.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        second_player.stamina -= first_player.stamina / 2
        if second_player.stamina <= 0:

            return f"Winner: {first_player.name}"

        first_player.stamina -= second_player.stamina / 2
        if first_player.stamina <= 0:

            return f"Winner: {second_player.name}"

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        else:
            return f"Winner: {second_player.name}"

    def next_day(self):

        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ''
        if self.players:
            for player in self.players:
                result += str(player) + '\n'
        if self.supplies:
            for supply in self.supplies:
                result += supply.details() + '\n'
        return result.strip()

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return supply, idx
        return None, -1
