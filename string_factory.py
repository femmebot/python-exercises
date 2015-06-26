# Create a function named string_factory that accepts a list of dictionaries and a string.
# Return a new list build by using .format() on the string, filled in by each of the dictionaries in the list.

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(my_dict, my_string):
    my_list = []

    for key in my_dict:
        my_list.append(my_string.format(**key))

    return(my_list)


string_factory(dicts, string)
print (string_factory(dicts, string))


# .value() to extract a dictionary's values for a key
for value in dicts[0].values():
    print (value)
