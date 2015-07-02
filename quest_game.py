# Create a game with a 2-dimensional map.
# Place the player, a door, and a monster into random spots in your map.
# Let the player move around in the map and, after each move,
# tell them if they've found the door or the monster.
# If they find either the game is over.
# The door is the win condition, the monster is the lose condition.

import random

# make a 6x6 grid
my_row = list('abcdef')
my_col = list(range(1,7))
coords = []
my_move = list(input('> '))

def make_grid(row, col):
    grid_list = []
    for row_item in row:
        for col_item in col:
            coords = row_item, col_item
            grid_list.append(coords)
    return(grid_list)

def generate_locations(coordinates):
    my_coords = coordinates[:]
    door = random.choice(my_coords)
    my_coords.remove(door)
    monster = random.choice(my_coords)
    # print(my_coords)
    # print(door, monster)
    return(door, monster)

def game_rules():
    print("You're in a 6x6 room, with cells A-F across and 1-6 from top to bottom.")
    print("You need to find the door by entering the secret cell coordinates, i.e., A1 for the top left cell. ")
    print("But, be careful and don't enter the coordinates for the monster instead!")
    print("Type HELP to view these rules, QUIT to end the game.")


# error-check input
# no more than 2 characters; require letter (A-F), then number (1-6)
#


# generate the coordinates for the game
game_coords = make_grid(my_row, my_col)
# print(make_grid(my_row, my_col))

# generate the coordinates for the door and the monster
generate_locations(game_coords)


#######

my_list = list(range(1, 51))
my_int = int(input('> '))
# my_int = random.randint(1,10)

def nchoices(my_iterable, n):
    counter = 0
    choices = []
    while counter < n:
        choices.append(random.choice(my_iterable))
        counter += 1
    return(choices)

nchoices(my_list, my_int)
print(nchoices(my_list, my_int))
