# TODO 1 : creating a class
class User: # class name in PascalCase
    # pass # you put this here when you have an empty class / function
    def __init__(self, user_id, username): # constructor
        self.id = user_id
        self.username = username
        self.followers = 0 # default value of 0
        # print("new user being created...")


user_1 = User("001", "corinne") # you have to add parenthesis to initialize an object from a class
user_2 = User("002", "jack") # you have to add parenthesis to initialize an object from a class

print(user_1.followers)
