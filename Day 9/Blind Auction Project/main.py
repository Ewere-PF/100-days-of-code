# TODO-1: Ask the user for input
import art
print(art.logo)
name= input("what is your name?:")
price= int(input("what is your bid?:"))

bids = {}

# TODO-2: Save data into dictionary {name: price}
bids[name] = price
# TODO-3: Whether if new bids need to be added
continue_bidding = True
while continue_bidding:
    name = input("what is your name?:")
    price = int(input("what is your bid?:"))
    bids[name] = price
    should_continue = input("Are they other bidders? (y/n)\n").lower()
    if should_continue == "n":
# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder

    print(f"The winner is {winner} with the highest bid of {highest_bidder}")




