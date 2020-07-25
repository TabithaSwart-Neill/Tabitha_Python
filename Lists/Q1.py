###
#
# Lists: Question 1
#
# Given the list of foods below, output the following:
# 1. The first item in the list.
# 2. The third item in the list.
# 3. The last item in the list.
# 4. The first three items in the list.
# 5. The last three items in the list.
# 6. The last item in the sublist.
# 
####

foods = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit",
"mango",
"kiwifruit"
]
print(foods[0])
print(foods[2])
print(foods[9])
print(foods[0:3])
print(foods[7:10])
print(foods[6][2])

