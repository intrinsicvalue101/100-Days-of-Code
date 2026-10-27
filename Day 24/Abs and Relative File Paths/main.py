# abs file paths begin at root
    # ex: ./Work/Project/talk.ppt
# relative is the directory you are currently in or present working directory
    # ex: ./talk.ppt

# absolute
# with open("/Users/Bob/PycharmProjects/100 Days of Code - The Complete Python Pro Bootcamp1/Day 24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # relative
with open("../my_file.txt") as file:
    contents = file.read()
    print(contents)

