my_list = [1, 2.5, 'a']
print (my_list)

length = len(my_list)
print ("My list length is {}".format(length))

my_sentence = "I'm a lumberjack and I'm OK! I sleep all night and I work all day!"

# see help (str.split())
# my_sentence.split()

sentence_list = my_sentence.split()
print (sentence_list)

joined_sentence = ' '.join(sentence_list)
print (joined_sentence)

split_sentence = my_sentence.split(sep="!")
print(split_sentence)
