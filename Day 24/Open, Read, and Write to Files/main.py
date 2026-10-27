# file = open("my_file.txt")
# contents = file.read() # returns string contents of file
# print(contents)
# file.close()

# if you don't want to have to manually close the file use this
    # with open("my_file.txt") as file: #automatically closes the file
    #     contents = file.read() # returns string contents of file
    #     print(contents)

# append allows you to add onto text
# write replaces text

# instead of reading a file lets write it
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")