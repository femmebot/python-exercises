# You count from 1 to a given number (let’s say 100). If the number is divisible by 3, instead of the number you say “fizz”.
# If it’s divisible by 5, you say “buzz”.
# And finally if it’s divisible by both 3 and 5, you say “fizz buzz”.
# Have a hard-coded upper line, n.
# Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
# Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
# Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
# Each number should be printed on a new line.

num = 1
upper_limit = int(input('Enter a number: '))

while num <= upper_limit:
    if num % 3 == 0 and num % 5 == 0:
        print('fizz buzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print (num)
    num += 1
