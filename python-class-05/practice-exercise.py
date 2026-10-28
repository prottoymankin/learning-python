# Given a list of roll numbers: [101, 105, 102, 101, 108, 105, 110]. Print all unique roll nums in the list.

roll_numbers = [101, 105, 102, 101, 108, 105, 110]

unique_roll_numbers = set(roll_numbers)

for roll_number in unique_roll_numbers:
  print(roll_number)

# Given Employee records in the form of a list of tuples where each tuple contains:
# (Employee ID, Employee Name, Salary)

"""
  Example - [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
  ]
"""

# Ask user to enter Employee ID and search it inside records.

employee_list = [
  (101, "Alice", 50000),
  (102, "Bob", 65000),
  (103, "Charlie", 45000)
]

is_employee_found = False

search_employee_id = int(input("Enter your Employee ID here: "))

for employee in employee_list:
  if (employee[0] == search_employee_id):
    print(employee)
    is_employee_found = True
    break

if is_employee_found == False:
  print("Employee not found.")