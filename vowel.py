# Write a script that takes for a word (or list of words),
# removes all of the vowels, and gives the word (or words) back.
# For example, if I give the script the word "Treehouse",
# I should get back "Trhs".

chars = ['A','E','I','O','U','a','e','i','o','u']

def remove_char(char_list):
    for item in char_list:
        while True:
            try:
                list_string.remove(item)
                # print(''.join(list_string))
            except:
                break
    print ("New vowel-less word/phrase: {}".format(''.join(list_string)))


print("\nEnter a word or phrase")
my_string = str(input("> "))
list_string = list(my_string)

remove_char(chars)
    
