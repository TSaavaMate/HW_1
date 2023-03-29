from character import Character


class Enemy(Character):

    def __init__(self, name: str, health: int, attack_power: int, gold_reward: int):
        self._gold_reward = gold_reward
        super().__init__(name, health, attack_power)

    def defeated(self):
        print(f"{self._name} is defeated")
        return self._gold_reward

    def __str__(self):
        return f'<{self._name}> (Health: <{self._health}>, Attack Power: <{self._attack_power}>,' \
               f'Gold Reward: <{self._gold_reward}>)' + "\n"
