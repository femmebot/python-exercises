import random
# import function_list

num_of_guesses = 0
random_num = 0
max_guesses = 5

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

while num_of_guesses < max_guesses:
    # print("Random number: {}".format(random_num))

    try:
        new_input = int(input("> "))
    except:
        print ("That's not a number. Try again.")
        break

    if new_input < 1 or new_input > 10:
        print("That number is outside the range of 1-10.")
        break

    num_of_guesses = num_of_guesses + 1

    if new_input == random_num:
        if num_of_guesses == 1:
            print("You guessed the number {} correctly in 1 guess!".format(random_num))
        else:
            print ("You guessed the number {} correctly in {} guesses!".format(random_num, num_of_guesses))
        break
    elif new_input < random_num:
        print ("Your guess is lower.")
        show_guesses()
        continue
    elif new_input > random_num:
        print ("Your guess is higher")
        show_guesses()
        continue



if num_of_guesses == 5:
    print("Sorry. You ran out of guesses. The correct number is {}.".format(random_num))


# player gets 5 chances
# if they guess wrong, indicate whether it's higher or lower
# tell them how many guesses they've made
