import random


class Character:
    def __init__(self, name: str, health: int, attack_power: int):
        self._name = name
        self._health = health
        self._attack_power = attack_power

    def attack(self, other):
        if isinstance(other, Character):
            damage = random.randint(1, self._attack_power)
            other.health -= damage
            print(f'<{self._name}> attacks <{other.name}> for <{damage}> damage!' + "\n")
        else:
            raise TypeError("wrong type of argument")

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health: int):
        self._health = new_health

    def __str__(self):
        return f'<{self._name}> (Health: <{self._health}>, Attack Power: <{self._attack_power}>)'
