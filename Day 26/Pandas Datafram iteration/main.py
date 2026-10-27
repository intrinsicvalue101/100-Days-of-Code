student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# TODO: Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

# TODO: Looping through dataframes --> think of dataframes as python dictionaries
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# for (key, value) in student_data_frame.items():
#     print(key)

# TODO: Loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)