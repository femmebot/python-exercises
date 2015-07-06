import random

from combat import Combat

COLORS = ['red', 'blue', 'yellow', 'green']


# everything in Python is an object
# objects or classes map to mental models

# class Monster:
class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience =1
    weapon = 'sword'
    sound = 'roar'
    # class attributes
    # hit_points = 1
    # color = 'yellow'
    # weapon = 'sword'
    # sound = 'roar'

    def __init__(self, **kwargs):
        # self.hit_points = kwargs.get('hit_points', 5)
        # self.sound = kwargs.get('sound', 'roar')
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

    def __str__(self):  # magic method that controls what happens when an object is turned into a string
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
        self.__class__.__name__,
        self.hit_points,
        self.experience)

        for key, value in kwargs.items():  # creates new attribute and value in console
            setattr(self, key, value)  #object/instance we want to set attribute on which is self

    # Methods are functions that belong to classes
    def battlecry(self):
        return self.sound.upper()

class Goblin(Monster):
    # pass
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'

class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    max_experience = 2
    max_experience = 6
    sound = 'growl'

class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaaaaaaaaaa'



# to import in console 'from monster import Monster'
# from [docname] import [classname]
# Monster.color

# to create an instance
# my_instance = Monster()

# to assign a new value to an attribute
# my_instance.hit_points = 5

#########
# Methods
#########
# >>> from monster import Monster
# >>> jabberwock = Monster()
# >>> jabberwock.battlecry()
# 'ROAR'
# >>> jabberwock.sound = 'tweet'
# >>> jabberwock.battlecry()
# 'TWEET'

###############
# Inheritance
###############
# >>> from monster import Monster
# >>> zombie = Monster()
# >>> zombie.color
# 'blue'
# >>> jab = Monster(color='yellow', sound='cry', power='2x')
# >>> jab.power
# '2x'
# >>> jab.color
# 'yellow'
# >>>

class Store(object):
    open = 9
    close = 10
    def hours(self):
        return (print("We're open from {} to {}.".format(self.open, self.close)))


class Zombie:
    # def __init__(self, hit_points=5, weapon='sword', color='blue'):
    #     self.hit_points = hit_points
    #     self.weapon = weapon
    #     self.color = color
    #     self.sound = sound

    def __init__(self, **kwargs):  # double-underscore is called a dunder
        self.hitpoints = kwargs.get('hit_points', 5)
        self.weapon = kwargs.get('weapon', 'sword')
        self.color = kwargs.get('color', 'blue')
        self.sound = kwargs.get('sound', 'roar')
    def battlecry(self):
        return self.sound.upper()

# >>> from monster import Zombie
# >>> flag_zombie = Zombie(weapon='flag')
# >>> flag_zombie.battlecry()
# 'ROAR'
# >>>
