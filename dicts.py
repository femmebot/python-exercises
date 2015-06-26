my_dict = { 'name': 'Kenneth'}

print (my_dict['name'])

phone_dict = { 'phone': { 'home': '201-222-7881', 'mobile': '703-867-1980'} }

print (phone_dict['phone'])
print (phone_dict['phone']['mobile'])

my_car = { 'color': 'blue'}
my_car['color'] = 'red'


# Write a function named members that takes two arguments,
# a dictionary and a list of keys. Return a count of how many
# of the items in the list are also keys in the dictionary.
# You can check for dictionary membership using the
# "key in dict" syntax from lists.

### Example
# my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
# my_list = ['apples', 'coconuts', 'grapes', 'strawberries']
# members(my_dict, my_list) => 2

sample_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
sample_list = ['apples', 'coconuts', 'grapes', 'strawberries']

def members(my_dict, my_list):
    count = 0
    for key in my_dict:
        for item in my_list:
            if key == item:
                print(key)
                count += 1
    print('Number of keys that are also list members: {}'.format(count))
    return(count)

members(sample_dict, sample_list)

my_account = {'username': 'femmebot', 'email': 'femmebot@gmail.com'}
my_account.update({'gender': 'female', 'firstname': 'Phoebe', 'lastname': 'Espiritu'})
print(my_account)

# Unpacking a dictionary
greeting = "Hello! My name is {firstname} and my username is {username}"
print(greeting.format(**my_account))


# Create a function named word_count() that takes a string.
# Return a dictionary with each word in the string as the key
# and the number of times it appears as the value.

# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

my_sentence = 'Hello Hello I am what I am'

def word_count(my_string):
    word_list = (my_string.lower()).split()
    my_dict = {}

    for item in word_list:
        my_dict.update({item: word_list.count(item)})

    return(my_dict)

word_count(my_sentence)
print(word_count(my_sentence))
