# TODO: Catching Exceptions --> try, except, else, finally
# FileNotFound
# with open("a_file.txt", ) as file:
#     file.read()

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#Type Error
# text = "abc"
# print(text + 5)

try: # 1st - try x
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
# note: excepts should catch a SPECIFIC situation
except FileNotFoundError: # 2nd - if x fails do this
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else: # 3rd - if x succeeds do this
    content = file.read()
    print(content)
finally: # last - do this no matter what happens.
    file.close()
    print("File was closed.")
    # raise TypeError("This is an error that I made up.") # raise our own exceptions

# TODO: Raise our own errors. common use case: user mistake
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)
