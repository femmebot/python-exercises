# Create a function named combo() that takes two iterables and returns a list of tuples.
# Each tuple should hold the first item in each list, then the second set, then the third,
# and so on. Assume the iterables will be the same length.

# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]
# If you use list.append(), you'll want to pass it a tuple of new values.
# Using enumerate() here can save you a variable or two.

# dict.items() - A method that returns a list of tuples from a dictionary.
# Each tuple contains a key and its value.

def combo(list1, list2):
    combined_list = []
    print(combined_list)
    for item1, item2 in enumerate(list2):
        print(item1, item2)
        temp_list = (list1[item1], item2)
        combined_list.append(temp_list)
    print(combined_list)
    return (combined_list)

list1 = ['swallow', 'snake', 'parrot']
list2 = ['a', 'b', 'c']
combo(list1, list2)

# alternate solution using zip()
list3 = zip(list1, list2)
print (list(list3))
# print(combo(combined_list))
