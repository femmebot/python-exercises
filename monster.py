# everything in Python is an object
# objects or classes map to mental models

# class Monster:
class Monster(object):
    # class attributes
    hit_points = 1
    color = 'yellow'
    weapon = 'sword'
    sound = 'roar'

    # Methods are functions that belong to classes
    def battlecry(self):
        return self.sound.upper()

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
