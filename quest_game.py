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

def make_grid(row, col):
    grid_list = []
    for row_item in row:
        for col_item in col:
            coords = row_item, col_item
            grid_list.append(coords)
    return(grid_list)

game_coords = make_grid(my_row, my_col)
# print(make_grid(my_row, my_col))

def generate_locations(coordinates):
    my_coords = coordinates[:]
    door = random.choice(my_coords)
    my_coords.remove(door)
    monster = random.choice(my_coords)
    # print(my_coords)
    # print(door, monster)
    return(door, monster)

generate_locations(game_coords)
