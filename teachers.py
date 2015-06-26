# Create a function named most_classes that takes
# a dictionary of teachers and returns the teacher with the most classes.

# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

treehouse_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
 'Kenneth Love': ['Python Basics', 'Python Collections','Write Better Python', 'Object-Oriented Python'], 'Phoebe Espiritu': ['Design & Code', 'Entrepreneurship', 'GitHub for Non-Programmers']}

def most_classes(my_dict):

    max_count = 0
    max_count_teacher = ''

    for key in my_dict:
        if len(my_dict[key]) >= max_count:
            max_count = len(my_dict[key])
            max_count_teacher = key
        print(key, len(my_dict[key]))
    return(max_count_teacher)


def num_teachers(my_dict):
    return(len(list(my_dict.keys())))


def stats(my_dict):
    teacher_list = []
    for key in my_dict:
        teacher_list.append([key, len(my_dict[key])])
        # print (teacher_list)
    return(teacher_list)


def courses(my_dict):
    course_list = []
    for value in my_dict.values():
        course_list = course_list + value
    # print(course_list)
    return(course_list)



most_classes(treehouse_dict)
print(most_classes(treehouse_dict))

num_teachers(treehouse_dict)
print(num_teachers(treehouse_dict))

stats(treehouse_dict)
print(stats(treehouse_dict))

courses(treehouse_dict)
print(courses(treehouse_dict))
