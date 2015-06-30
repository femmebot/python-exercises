# simultaneous assignment
a, b = 1, 2

c = (3, 4)

d, e = c

def my_func():
    return 1, 2, 3


tup = my_func

x, y, z = my_func()


# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?

def stringcases(my_string):
    uppercased = my_string.upper()
    lowercased = my_string.lower()
    titlecased = my_string.title()
    reverso = list(my_string)[::-1]
    # reverso = [::-1]
    reversed_string = ''.join(reverso)
    return uppercased, lowercased, titlecased, reversed_string

string_input = input('> ')
stringcases(string_input)
print(stringcases(string_input))


# enumerate() A function that takes a iterable, like a list,
# and gives back a list of tuples where each tuple holds
# the index of the item and its value.

my_account = {'username': 'femmebot', 'email': 'femmebot@gmail.com'}
my_account.update({'gender': 'female', 'firstname': 'Phoebe', 'lastname': 'Espiritu'})
alpha_list = list('abcdefghijklmnopqrstuvwxyz')

for index, letter in enumerate(alpha_list):
    print('{}: {}'.format(index, letter))

# step is a tuple
for step in enumerate(alpha_list):
    print('{}: {}'.format(step[0], step[1]))

for step in enumerate(alpha_list):
    print('{}: {}'.format(*step)) # one star unpacks tuples or lists; 2 stars, dicts

# dict.items() - A method that returns a list of tuples from a dictionary.
# Each tuple contains a key and its value.
for key, value in my_account.items(): # loop through and unpack tuples from a dictionary
    print('{}: {}'.format(key.title(), value))
