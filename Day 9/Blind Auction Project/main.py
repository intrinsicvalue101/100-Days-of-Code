from operator import truediv
import art

print(art.logo)

# Dictionary of bids
bids = {
        }

# TODO-1: Ask the user for input
def ask_for_bids():
    name = input("What's your name?: ")
    bid = input("What's your bid$?: ")
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid
    #print(bids)

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bids):
    highest_value = 0
    for bidder in bids:
        value = int(bids[bidder])
        if value > highest_value:
            highest_value = value
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_value}.")

ask_for_bids()

continue_bidding = True

while continue_bidding:

    # TODO-3: Whether if new bids need to be added
    new_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if new_bids == "yes":
         print("\n" * 20)
         ask_for_bids()
    else:
        find_highest_bidder(bids)
        continue_bidding = False # exit the program


