from character import Character


class Player(Character):
    def __init__(self, name: str, health: int, attack_power: int, gold: int):
        self._gold = gold
        super().__init__(name, health, attack_power)

    def collect_gold(self, amount: int):
        if amount>0:
            self._gold += amount
            print(f'<{self._name}> has collected <{amount}> gold!' + "\n")
        else:
            raise ValueError("amount shouldn't be negative")

    def __str__(self):
        return f'<{self._name}> (Health: <{self._health}>, Attack Power: <{self._attack_power}>, Gold: <{self._gold}>)'

    @property
    def gold(self):
        return self._gold
