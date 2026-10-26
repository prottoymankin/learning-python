# Type casting
# Type casting means explicitly converting one data type to another.
age = "25" # str
new_age = int(age) # int
new_float_age = float(age) # 25.0 (float)

# Here, Python automatically converts the integer value 1 into the float value 1.0
# because it is performing a calculation with a float value (2.5).
# This is called implicit type conversion.
result = 1 + 2.5 # 3.5 (float)

# Simple sum program
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum = a + b
# print("Sum: ", sum)

# String methods -> String methods are used to perform operations on strings.
# Strings are immutable in Python, which means we cannot modify or update the original string after it is created.
name = "Tony Stark"
name.upper() #converts all characters to uppercase.
name.lower() #converts all characters to lowercase.

# find() is a string method used to find a substring within a string.
# It returns the index of the first occurrence of the substring.
# If the substring is not found, it returns -1.
name.find("ta")

# The replace() method is used to replace a substring with another string.
# replace() returns a new string and does not modify the original string
text = "Hello World!"
text.replace("World", "Python") # Hello Python!

# We use the 'in' operator to check whether a substring is present in a string.
# Returns True if the substring is present, otherwise False.
("ll" in text) # True
("X" in text) # False