import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to set difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

random_integer = random.randint(1,100)

while attempts != 0:
    print(f"You have {attempts} to guess the number")
    guess = int(input("Make a guess: "))
    if guess > random_integer:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
    elif guess < random_integer:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
    elif guess == random_integer:
        print(f"You got it! The answer was {random_integer}.")
        attempts = 0
