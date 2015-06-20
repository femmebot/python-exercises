import random
# import function_list

num_of_guesses = 0
random_num = 0

# generate a random number between 1 and 10
# def generate_random_num():
#     random_num = random.randint(1,10)
#     print(random_num)
#     return random_num

def instructions():
    print("I picked a number from 1-10. You have 5 chances to guess the number.")

def show_guesses():
    if num_of_guesses == 1:
        print("You made {} guess.".format(num_of_guesses))
    else:
        print("You made {} guesses.".format(num_of_guesses))

instructions()
random_num = random.randint(1,10)
# print(random_num)

while num_of_guesses < 5 :
    new_input = int(input("> "))
    num_of_guesses = num_of_guesses + 1
    print("Random number: {}".format(random_num))

    if new_input == random_num:
        print ("You guessed the number {} correctly!".format(random_num))
        break
    elif new_input < random_num:
        print ("Your guess is lower.")
        show_guesses()
        continue
    elif new_input > random_num:
        print ("Your guess is higher")
        show_guesses()
        continue
    else:
        print ("That's not a number. Try again.")


if num_of_guesses == 5:
    print("Sorry. You ran out of guesses. The correct number is {}.".format(random_num))


# player gets 5 chances
# if they guess wrong, indicate whether it's higher or lower
# tell them how many guesses they've made
