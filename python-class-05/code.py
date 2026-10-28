# List
# A list can store multiple values in a single variable.
marks = [90, 98, 88, 86]

# A list can store multiple values of the same or different data types.
mixedValues = [13, 99.99, 'A', True]

values = [10, 10.5, 'hello', True]

# The len() function returns the number of items in a list.
len(values) # Output: 4

# Slicing a list
values[0:3] # Output: [10, 10.5, 'hello']

# loop in a list
for value in values:
  print(value)

# List is mutable - we can add, delete or change the values of a list
# The append() method adds an item to the end of a list.
values.append(90) # Output: [10, 10.5, 'hello', True, 90]

# The insert() method adds an item at a specific position in a list.
values.insert(2, 35) # Output: [10, 10.5, 35, 'hello', True, 90]

# The in operator checks whether an item exists in a list.
print("hello" in values) # Output: True
print(100 in values) # Output: False

# The clear() method removes all items from a list.
values.clear()
print(values) # Output: []


# Tuples - Immutable
# Tuples are immutable, so we cannot add, remove, or modify items after creation.
tuple_values = (10, 20, 10, 30, 40, 50, 10)

# The count() method returns how many times a value appears in a tuple.
tuple_values.count(10) # Output: 3

# The index() method returns the index of the first occurrence of an item in a list or tuple.
list_values = [10, 20, 10, 30, 40, 50, 10]
list_values.index(10) # Output: 0
tuple_values.index(10) # Output: 0

# Parentheses are optional when creating a tuple.
numbers = 10, 20, 30
type(numbers)  # <class 'tuple'>

# Set
# A set is a collection of unique items with no duplicate values.
set_values = {98, 94, 99, 91, 92}

for value in set_values:
  print(value)

# Dictionary
# A dictionary stores data as key-value pairs.
person = {
  "name": "John Doe",
  "age": 24,
  "isMarried": False
}

# We use a key to access its corresponding value in a dictionary.
person["name"]
person["isMarried"]

# We can update a dictionary value by assigning a new value to its key.
person["name"] = "Harry Potter" # Output: {'name': 'Harry Potter', 'age': 24, 'isMarried': False}

# We can add a new key-value pair to a dictionary by assigning a value to a new key.
person["country"] = "United States America"

# loop on a dictionary
for key in person:
  print(key, person[key])