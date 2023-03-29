from enemy import Enemy
from game import Game
from player import Player

player = Player(name="pochita", health=300, attack_power=150, gold=0)

enemies = [Enemy(name="goblin", health=30, attack_power=10, gold_reward=10),
           Enemy(name="Dragon", health=15, attack_power=15, gold_reward=20),
           Enemy(name="makima", health=50, attack_power=100, gold_reward=30),
           Enemy(name="galgali", health=20, attack_power=70, gold_reward=40),
           Enemy(name="power", health=50, attack_power=60, gold_reward=50)]
game = Game(player)
for enemy in enemies:
    game.add_enemy(enemy)
game.play()
