student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO: an index is the label used to identify each row in a DataFrame or Series.
#  Think of it like the row header in a table or the key in a dictionary.

# TODO: Columns = fields (name, score, etc.), vertical

# TODO: Rows = one full entry (one person, one item, one observation), horizontal

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data_frame)
phonetic_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()} # dictionary comprehension to iterate through each row in data frame
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word] # try out this line
    except KeyError: # catch the exception
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()