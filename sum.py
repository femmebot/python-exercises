# add_list([1, 2, 3]) should return 6
# summarize([1, 2, 3]) should return "The sum of [1, 2, 3] is 6."
# Note: both functions will only take *one* argument each.

num_list = [1,2,3,4]

def add_list(num_list):
    sum = 0
    for item in num_list:
        sum = sum + item
    print(sum)
    return(sum)

def summarize(num_list):
    print("The sum of {} is {}".format(num_list, add_list(num_list)))
    return("The sum of {} is {}".format(num_list, add_list(num_list)))

summarize (num_list)
