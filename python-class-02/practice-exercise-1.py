# Take price 0f 3 products as input (eg- 99.5, 23.75, 16.15)
#   - print the total Bill amount
#   - print the average price
# Take the superhero name as input & check if it starts with "S" / 's' or not.

price_1 = float(input("Enter first price: "))
price_2 = float(input("Enter second price: "))
price_3 = float(input("Enter third price: "))

total_bill = price_1 + price_2 + price_3
average_price = total_bill / 3

print("Total Bill:", total_bill)
print("Average Price:", average_price)

superhero_name = input("Enter superhero name: ")

print(superhero_name.startswith(('S', 's')))

# The startswith() method checks whether a string starts with a specified substring.
# The startswith() method accepts multiple prefixes in a tuple.
# It returns True if the string starts with any one of them,
# similar to the OR operator.