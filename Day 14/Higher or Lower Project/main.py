import random
from game_data import data
import art

# Function that returns whichever follower count is higher
def find_higher_followers(first_follower_count,second_follower_count):
    if first_follower_count > second_follower_count:
        answer = first_follower_count
    else:
        answer = second_follower_count
    return answer

# Function that checks if the user's guess matches the correct answer.
def compare(user_guess, answer):
    if user_guess > answer or user_guess < answer:
        return False
    else:
        return True

score = 0 # Keeps track of how many times the user guesses correctly

def game():
    # If you try to modify a global variable inside a function,
    # Python will treat that variable as local unless you explicitly declare it as global
    global score # Allow score to update inside the function
    global first_choice # Carry over the previous winner into the next round

    account_b = random.choice(data) # Select a random account for option B
    second_choice = "Against B: " + account_b["name"] + ", a " + account_b["description"] + ", from " + account_b["country"] + "."
    followers_b = data[data.index(account_b)]["follower_count"] # Store B’s follower count

    print("\n" * 20) # clear the screen
    print(art.logo) # Display the game logo, the first comparison option (A), and the second option (B)
    print(first_choice)
    print(art.vs)
    print(second_choice)

    question = input("Who has more followers? Type 'A' or 'B': ").upper() # Ask user for their guess

    if question == "A":
        user_guess = followers_a # Store follower count of A as user’s guess
    else:
        user_guess = followers_b # Store follower count of B as user’s guess

    answer = find_higher_followers(followers_a, followers_b) # Determine which account actually has more followers
    verify_guess = compare(user_guess, answer) # Check if user's guess matches the correct answer

    if verify_guess == True:
        score += 1 # Increase score for each correct guess
        print(f"You're right! Current score {score}.")

        # Update option A to be the previous round’s winner
        if answer == followers_b:
            first_choice = "Compare A: " + account_b["name"] + ", a " + account_b["description"] + ", from " + account_b["country"] + "."
        elif answer == followers_a:
            first_choice = "Compare A: " + account_a["name"] + ", a " + account_a["description"] + ", from " + account_a["country"] + "."

        game() # Continue the game with new A and random B
    else:
        print("Sorry, that's wrong.") # End the game if the guess is incorrect

account_a = random.choice(data) # Randomly select first account for option A
first_choice = "Compare A: " + account_a["name"] + ", a " + account_a["description"] + ", from " + account_a["country"] + "."
followers_a = data[data.index(account_a)]["follower_count"]
game() #  start the game!


# print(game_data.data[0]["name"]) #access key within single dictionary
# print(random.choice(game_data.data)) # grab random dictionary within nested dictionary
