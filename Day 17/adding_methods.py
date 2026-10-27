# TODO 2 : adding methods to a class
class User:
    def __init__(self, user_id, username): # constructor
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): #methods always have to have self parameter, unlike functions
        user.followers += 1
        self.following += 1

user_1 = User("001", "corinne")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)