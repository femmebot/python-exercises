my_dict = { 'name': 'Kenneth'}

print (my_dict['name'])

phone_dict = { 'phone': { 'home': '201-222-7881', 'mobile': '703-867-1980'} }

print (phone_dict['phone'])
print (phone_dict['phone']['mobile'])


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
