import sys

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
            if input('Dodge? Y/N').lower() == 'y':
                # If so, check whether dodging was successful
                if self.player.dodge():
                    # If it is, move on
                    print('You dodged the attack!')
                else:
                    # If not, remove one player hit point
                    print('Bummer. You got hit anyway.')
                    self.player.hit_points -= 1
            else:  # if player doesn't opt to dodge
                print('{} hit you for 1 point.'.format(self.monster))
                self.player.hit_points -= 1
            # If the monster isn't attacking, inform the player
        else:
            print("{} isn't attacking.".format(self.monster))


    def player_turn(self):
        # let the player attack, rest or quit
        player_choice = input('[A]ttack, [R]est, or [Q]uit?').lower()
        # if they attack:
        if player_choice == 'a':
            print("You're attacking {}.".format(self.monster))
            # see if the attack is successful
            if self.player.attack():
                # If so, see if the monster dodges
                if self.monster.dodge():
                    # If dodged, print that
                    print('{} dodged the attack'.format(self.monster))
                    # If not dodged, subtract the right number of hit points from the monster
                else:
                    if self.player.leveled_up():
                        self.monster.hit_point -= 2
                    else:
                        self.monster.hit_points -= 1
                    print('You attacked and hit {} with your {}'.format(self.monster, self.player.weapon))
            else:
                print("You missed.")
        # If they rest, call the player rest() method
        elif player.choice == 'r':
            self.player.rest()
        # If they quit, end game
        elif player.choice == 'q'
            sys.exit()
        # If they pick an ything else, re-run this method
        else:
            self.player_turn()

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
