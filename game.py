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
        # check to see if monster attacks
        if self.monster.attack():
            # if so, tell the player
            print("{} is attacking!".format(self.monster)
            # Check if the player wants to dodge
            
            # If so, check whether dodging was successful
                # If it is, move on
                # If not, remove one player hit point
            # If the monster isn't attacking, inform the player

    def player_turn(self):
        # let the player attack, rest or quit
        # if they attack:
            # see if the attack is successful
                # If so, see if the monster dodges
                    # If dodged, print that
                    # If not dodged, subtract the right number of hit points from the monster
                # If they rest, call the player rest() method
                # If they quit, end game
                # If they pick anything else, re-run this method

    def cleanup(self):
        # If the monster has no more hit points:
            # increase player's experience
            # print a message
            # get a new monster

    def __init__(self):
        self.setup()

        while self.player.hitpoints and (self.monster or self.monsters):
            print(self.player)
            self.monster.turn()
            self.player_turn()
            self.cleanup()

        if self.player.hitpoints:
            print('You win!')
        elif self.monster or self.monsters:
            print('You lose.')
