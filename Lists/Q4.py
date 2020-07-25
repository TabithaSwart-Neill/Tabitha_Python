###
#
# Lists: Question 4
#
# 1. Ask the user to enter a string.
# 2. Split the string into a list, divided by spaces 
#     (hint: yourlist.split() will be useful).
# 3. Convert the string to a list, where each character is an item in the list 
#     (hint: list(yourlist) will be useful).
# 4. For each list: output the length of the list, and the list itself.
# 
# 

mystring = input(print(f"Please enter a string of characters here: "))

mylist = mystring.split(' ')
def split(mylist):
    return[char for char in mylist]

print(mystring)
print(split(mystring))
