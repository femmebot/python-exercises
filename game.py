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
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:  # handles case where list is empty
            return None

    def monster_turn(self):
        # check to see if mosnter attacks
        # if so, tell the player
            # Check if the player wants to dodge
            # If so, check whether dodging was successful
                # If it is, move on
                # If not, remove one player hit point
            # If the monster isn't attacking, inform the player
            
