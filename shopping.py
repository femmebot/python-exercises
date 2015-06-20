shopping_list = list()
my_list = ""
count = 1

print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break

    shopping_list.append(new_item)
    print("Added! List has {} items.".format(len(shopping_list)))
    continue

print("Here's your list:")

for item in shopping_list:
    # print(item)
    if count == len(shopping_list):
        my_list = my_list + item
    else:
        my_list = my_list + item + ", "
        # count = count + 1
        count += 1

print(my_list)
