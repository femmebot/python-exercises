# Create a function named combo() that takes two iterables and returns a list of tuples.
# Each tuple should hold the first item in each list, then the second set, then the third,
# and so on. Assume the iterables will be the same length.

# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]
# If you use list.append(), you'll want to pass it a tuple of new values.
# Using enumerate() here can save you a variable or two.

def combo(my_combo):
    new_combo = []
    for step in enumerate(my_combo):
        new_combo.append((step[1]))
    return(new_combo)

combined_list = (['swallow', 'snake', 'parrot'], ['a', 'b', 'c'])
combo(combined_list)
print(combo(combined_list))
