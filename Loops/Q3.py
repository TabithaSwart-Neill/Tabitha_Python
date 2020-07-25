###
#
# Loops: Question 3
#
# Use a while loop to ask the user for three names and 
# append them to a list, then 
# use a for loop to print the list.

name_collection = []
counter = 0

# The while loop
while counter < 3:
    name = input(print(f"Please enter a name :"))
    name_collection.append(name)
    counter += 1

# The for loop
for index, item in enumerate(name_collection):
    print(index, item)


