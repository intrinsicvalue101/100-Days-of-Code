# TODO: Basic dictionary comprehension
#  new_dict = {new_key:new_value for item in list}

# TODO: create a new dictionary based off of existing dictionary
#  new_dict = {new_key:new_value for (key,value) in dict.items()}

# TODO: add a condition
#  new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# The primary use of items() is to iterate over both the keys and the values of a dictionary simultaneously, typically using a for loop and tuple unpacking.

import random

#generate a random student score by looping through list of names
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor","Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score > 69}
print(passed_students)

# To convert a sentence into a list of words in Python, the most straightforward and common approach is to use the built-in string method .split()