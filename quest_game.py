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

def make_grid(row, col):
    grid_list = []
    for row_item in row:
        for col_item in col:
            temp_list = row_item, col_item
            grid_list.append(temp_list)
    return(grid_list)

make_grid(my_row, my_col)
print(make_grid(my_row, my_col))
