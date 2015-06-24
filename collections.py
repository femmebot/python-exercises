
# Make a function named first_4 that accepts an iterable as an argument
# and returns the first 4 items in the iterable.
clean_list = [-1, 0, 1, 2, 3, 4, 5, 7, 8, 9]
print ("clean_list: {}".format(clean_list))

def first_4(my_list):
    return(my_list[:4])

first_4(clean_list)
print(first_4(clean_list))


# Make a function named odds that accepts an iterable as an argument
# and returns the items with an odd index in the iterable.

def odd_indeces(my_list):
    return(my_list[1::2])

odd_indeces(clean_list)
print(odd_indeces(clean_list))


# Make a function name first_and_last_4 that accepts an iterable
# and returns the first 4 and last 4 items in the iterable.

def first_and_last_4(my_list):
    last_four = my_list[len(my_list)-len(my_list)-4:len(my_list)]
    return(first_4(my_list)+last_four)

first_and_last_4(clean_list)
print("Combined: {}".format(first_and_last_4(clean_list)))


# Exercises with deleting, replacing lists

mixed_list = [1,2,'a','b','c','d',5,6,7,'f','g','h',8,9,'j']
del mixed_list[:2]
mixed_list[4:7] = ['e']
mixed_list[8:10] = ['i']
print(mixed_list)


# The first half of the string, rounded with round(), should be lowercased.
# The second half should be uppercased.
# E.g. "Treehouse" should come back as "treeHOUSE"
sample_string = 'Treehouse'

def sillycase(my_string):
    first_half_idx = round(len(my_string)/2)
    return(my_string[:first_half_idx].lower()+my_string[first_half_idx:].upper())

sillycase(sample_string)
print (sillycase(sample_string))
