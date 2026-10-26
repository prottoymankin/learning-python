# Arithmetic Operators
addition = 5 + 5
subtraction = 10 - 5
multiplication = 5 * 5
division = 25 / 5

# The // operator returns only the integer part of the division.
result = 7 // 3 # Output: 3

modulo = 5 % 3
power = 5 ** 3 # 5^3

# Assignment Operator
x = 1
x += 5 # Equivalent to x = x + 5
x -= 1 # Equivalent to x = x - 1
x *= 2 # Equivalent to x = x * 2

#Comparison Operators
3 > 2 # Output: True
3 < 2 # Output: False
3 >= 3 # Output: True
3 <= 5 # Output: True

3 == 3 # Output: True
3 == 4 # Output: False

3 != 2 # Output: True
3 != 3 # Output: False

# Logical Operators
print(True or False) # True
print(True or True) # True
print(False or True) # True
print(False or False) # False

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(not True) # False
print(not False) # True

# Conditionals (if-else)
age = 24

if age >= 18:
  print("You are an adult.")
else:
  print("You are not an adult.")

mark = 80

if mark >= 80:
  print('A')
elif mark < 80 and mark >= 60:
  print('B')
else:
  print('C')
