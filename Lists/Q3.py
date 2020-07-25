###
#
# Lists: Question 3
#
# 
# Ask the user for three names, 
# append them to a list, 
# then print the list.
#
#

name_collection = []
counter = 0
while counter < 3:
    name = input(print(f"Please enter a name for position {counter}"))
    name_collection.append(name)
    counter += 1
print(name_collection)





