import random

from enemy import Enemy
from player import Player


class Game:
    def __init__(self, player: Player):
        if isinstance(player, Player):
            self._player = player
            self._enemies = []
        else:
            raise TypeError("wrong type of argument")

    def add_enemy(self, enemy: Enemy):
        if isinstance(enemy, Enemy):
            self._enemies.append(enemy)
        else:
            raise TypeError("wrong type of argument")

    def play(self):
        print(f'Welcome, <{self._player.name}>!' + "\n")

        enemy = self.__choose_enemy()

        while self._player.health > 0:
            print(self._player)
            print(enemy)

            self._player.attack(enemy)

            if enemy.health <= 0:
                self._player.collect_gold(enemy.defeated())
                self._enemies.remove(enemy)
                enemy = self.__choose_enemy()
            else:
                enemy.attack(self._player)

            if len(self._enemies) == 0:
                print(f'Congratulations, <{self._player.name}>! You have defeated all enemies and'
                      f' won the game with <{self._player.gold}> gold.')
                return

        print(f"<{self._player.name}> has been defeated! Game over.")

    def __choose_enemy(self) -> Enemy | None:
        num_of_enemies = len(self._enemies)

        if num_of_enemies == 1:
            enemy = self._enemies[0]
            print(f' A wild <{enemy.name}> appears!')
        elif num_of_enemies < 1:
            print("no enemies left")
            return None
        else:
            random_enemy = random.randrange(0, num_of_enemies)
            enemy = self._enemies[random_enemy]
            print(f' A wild <{enemy.name}> appears!' + "\n")

        return enemy
