# Below is a list of foods and their prices per unit:
# groceries = [
# ["Baby Spinach", 2.78],
# ["Hot Chocolate", 3.70],
# ["Crackers", 2.10],
# ["Bacon", 9.00],
# ["Carrots", 0.56],
# ["Oranges", 3.08]
# ]
# Ask the user how many units of each item they bought, then 
# output the corresponding receipt.
# For the input below, assume that the input is provided 
# in the same order as defined in the list above.

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]    

groceries = [x + [0] for x in groceries]

# # how to get the number of itterations you have done
for index, item in enumerate(groceries):
    item[2] = input(print(f"How many did you buy of the {item[0]}?"))

# format a receipt
sum = float(0)
print("====Izzy's Food Emporium====")
for item in groceries:
    item[1] = int(item[2]) * item[1]
    sum = float(sum) + item[1] 
    print(f"{item[0]:<20} ${item[1]:.2f}")
print("============================")
# format the sum as float with a dollar sign included :)
currency = "${:,.2f}".format(sum)
print(f"{currency:>27}")

