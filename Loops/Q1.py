# Continuously ask the user to enter a number until they 
# provide a blank input. Output the sum of all the numbers.

# total = int(0)
# num = input("Enter a number please ")
# while num.isdigit():
#     total = int(total) + int(num)
#     num = input("Enter a number please ")
# else:
#     print(f"Total = {total}")

total = int(0)
num = input("Enter a number please ")
while num.lstrip("-").isdigit():
    total = total + int(num)
    num = input("Enter a number please ")
print(total)

