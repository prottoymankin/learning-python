# Write a function to check if a number is odd or even.
def check_number (number):
  if (number % 2 == 0):
    return "Even"
  else:
    return "Odd"

# WAF to count the number of vowels in a string.
def count_vowels (string):
  count = 0

  for character in string.lower():
    if character in "aeiou":
      count += 1

  return count

# WAF to print if a number is prime or not.
import math

def check_prime (number):
  if number <= 1:
    print(number, "is not prime.")
    return

  for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
      print(number, "is not prime.")
      return

  print(number, "is prime.")

# WAF to return the average marks if a list of marks is passed as paremeter.

def calc_average (marks):
  if len(marks) == 0:
    print("Average: 0")

  # The sum() function returns the sum of numeric values in an iterable.
  average = sum(marks) / len(marks)

  print("Average:", average)