# Create a game with a 2-dimensional map.
# Place the player, a door, and a monster into random spots in your map.
# Let the player move around in the map and, after each move,
# tell them if they've found the door or the monster.
# If they find either the game is over.
# The door is the win condition, the monster is the lose condition.

import random

# make a 6x6 grid
x_row = list(range(1,7))
y_col = list(range(1,7))
player = []
# my_move = list(input('> '.upper()))

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
    my_coords.remove(monster)
    player = random.choice(my_coords)
    print(my_coords)
    return(door, monster, player)

def game_rules():
    print("You're in a 6x6 grid, with x 1 - 6 rows across and y 1 - 6 columns from top to bottom.")
    print("You need to move UP, DOWN, LEFT or RIGHT to find the door.")
    print("But, be careful and don't enter the coordinates for the monster instead!")
    print("Type HELP to view these instructions, QUIT to end the game.")

# Get player's current location
# Check to see if location is at the edge, i.e., x or y is at 1 or 6
# and only permit moves that are within bounds
def check_bounds(player_coords):
    if player_coords[0] == 1:
        left_flag = True
    elif player_coords[0] == 6:
        right_flag = True
    if player_coords[1] == 1:
        up_flag = True
    elif player_coords[1] == 6:
        down_flag = True
    if left_flag and up_flag:
        print('Your current location is: {}. Type RIGHT or DOWN to move.'.format(player))
    if left_flag and down_flag:
        print('Your current location is: {}. Type RIGHT or UP to move.'.format(player))
    if right_flag and up_flag:
        print('Your current location is: {}. Type LEFT or DOWN to move.'.format(player))
    if right_flag and down_flag:
        print('Your current location is: {}. Type LEFT or UP to move.'.format(player))
    if left_flag:
        print('Your current location is: {}. Type RIGHT, UP or DOWN to move.'.format(player))
    if right_flag:
        print('Your current location is: {}. Type LEFT, UP or DOWN to move.'.format(player))
    if up_flag:
        print('Your current location is: {}. Type LEFT, RIGHT or DOWN to move.'.format(player))
    if down_flag:
        print('Your current location is: {}. Type LEFT, RIGHT or UP to move.'.format(player))
    else:
        print('Your current location is: {}. Type LEFT, RIGHT, UP or DOWN to move.'.format(player))






# generate the coordinates for the game
game_coords = make_grid(x_row, y_col)
# print(make_grid(my_row, my_col))

# generate the coordinates for the door and the monster
generate_locations(game_coords)
print(generate_locations(game_coords))
print('player: {}'.format((generate_locations(game_coords)[2])))
# If LEFT, y = -1. If RIGHT, y = +1
# If UP, x = -1. If DOWN, x = +1
# error-check input
check_bounds(player)

def move(your_move):
    while your_move != 'QUIT':
        if your_move == 'HELP':
            game_rules()



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
