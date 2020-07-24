# Use a while loop to ask the user for three names and 
# append them to a list, then 
# use a for loop to print the list.

name_collection = []
counter = 0
while counter < 3:
    name = input(print(f"Please enter a name :"))
    name_collection.append(name)
    counter += 1

for index, item in enumerate(name_collection):
    print(index, item)


