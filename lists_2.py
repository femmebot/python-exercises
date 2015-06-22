the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
the_list.insert(0,the_list.pop(3))

the_list_copy = the_list[:]

for item in the_list_copy:
    if type(item) is not int:
        the_list.remove(item)

the_list.extend(range(4,21))

print(the_list)
