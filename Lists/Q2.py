###
#
# Lists: Question 2
#
# Format and print the following list:
# 
# mailing_list = [
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Biscuit", "biscuit@whippies.park"],
# ["Rory", "rory@whippies.park"],
# ]
# 
#### code below ...


mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

for counter, item in enumerate(mailing_list):
    print(counter, item)

print()

for item in mailing_list:
    print(f"{item[0]}: {item[1]}")
