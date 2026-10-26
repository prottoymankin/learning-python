# Print all odd numbers from 1 to 20

for i in range(1, 21, 2):
  print(i)

# Print the table of 57

for i in range (1, 11):
  print(i * 57)

# Print all multiples of 3 from 1 to 50 but skip 15

for i in range(3, 51, 3):
  if i == 15: continue
  print(i)

# Take two integers a and b as input
# Find and print the first number between 1 to 1000 that is divisible by both numbers.

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

if a <= 0 or b <= 0:
  print("Invalid input")
else:
  for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
      print(i)
      break

