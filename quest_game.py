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
grid_list = []
# my_move = list(input('> '.upper()))

def make_grid():

    for row_item in x_row:
        for col_item in y_col:
            coords = row_item, col_item
            grid_list.append(coords)
    return(grid_list)

def generate_locations():
    my_coords = grid_list[:]
    door = random.choice(my_coords)
    my_coords.remove(door)
    monster = random.choice(my_coords)
    my_coords.remove(monster)
    init_pos = random.choice(my_coords)
    print(door, monster, init_pos)
    return door, monster, init_pos


def game_rules():
    print("You're in a 6x6 grid, with x 1 - 6 rows across and y 1 - 6 columns from top to bottom.")
    print("You need to move UP, DOWN, LEFT or RIGHT to find the door.")
    print("But, be careful and don't enter the coordinates for the monster instead!")
    print("Type HELP to view these instructions, QUIT to end the game.")


# Get player's current location
# Check to see if location is at the edge, i.e., x or y is at 1 or 6
# and only permit moves that are within bounds

def check_bounds():
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    # If player x-coordinate is at 1, remove LEFT
    if x == 1:
        moves.remove('LEFT')
    # If player x-coordinate is at 6, remove RIGHT
    if x == 6:
        moves.remove('RIGHT')
    # If player y-coordinate is at 1, remove UP
    if y == 1:
        moves.remove('UP')
    # If player y-coordinate is at 6, remove DOWN
    if y == 6:
        moves.remove('DOWN')
    print('Your current position is: {}, {}. You can move {}.'.format(x, y, moves))
    return moves


# If LEFT, y = -1. If RIGHT, y = +1
# If UP, x = -1. If DOWN, x = +1
# error-check input

# generate the coordinates for the game
game_coords = make_grid()
print(make_grid())

# generate the coordinates for the door and the monster
door, monster, player = generate_locations()
print('door: {} monster: {} player: {}'.format(door, monster, player))
x, y = player

check_bounds()

while True:
    move = (input('> ')).upper()

    print(move)

    if move == 'QUIT':
        break

    if move == 'HELP':
        game_rules()
        
    elif move in check_bounds():
        if move == 'LEFT':
            x -= 1
        elif move == 'RIGHT':
            x += 1
        elif move == 'UP':
            y -= 1
        elif move == 'DOWN':
            y += 1
        print(x,y)
    else:
        print("That's not a valid move. Try {}.".format(check_bounds()))

    check_bounds()





#######
#
# my_list = list(range(1, 51))
# # my_int = int(input('> '))
# my_int = random.randint(1,10)
#
# def nchoices(my_iterable, n):
#     counter = 0
#     choices = []
#     while counter < n:
#         choices.append(random.choice(my_iterable))
#         counter += 1
#     return(choices)
#
# nchoices(my_list, my_int)
# print(nchoices(my_list, my_int))
