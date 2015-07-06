from character import Character
# from monster import Goblin, Troll, Dragon
from monster import Dragon
from monster import Goblin
from monster import Troll

class Game(object):
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
