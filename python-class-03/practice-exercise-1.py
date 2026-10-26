# Mini-Project: Calculator
# Build a Calculator that can perform following operations
# a + b
# a - b
# a * b
# a / b
# a % b
# a ** b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter an operator your want to perform: (+, -, *, /, %, **): ")

if operator == '+':
  print("Addition:", a + b)
elif operator == '-':
  print("Subtraction:", a - b)
elif operator == '*':
  print("Multiplication:", a * b)
elif operator == '/':
  print("Division:", a / b)
elif operator == '%':
  print("Modulo:", a % b)
elif operator == "**":
  print("Power:", a ** b)
else:
  print("Invalid operation")