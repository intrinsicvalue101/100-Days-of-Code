# List Comprehension = case where you create a new list from a previous list in less lines of code

# TODO: basic structure
#  new_list = [new_item for item in list]

numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

# List comprehension works with python sequences --> list, range, string, tuple
name = "Angela"
letters_list = [letter for letter in name]

range_list = [num*2 for num in range(1,5)]

#TODO: test case structure
# new_list = [new_item for item in list if test_case]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]