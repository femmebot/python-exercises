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
