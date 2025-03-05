# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
from art import congratulations


def find_highest_bidder(dictionary):
    winner = ""
    highest_bidder = 0
    for i in dictionary:
        bid_amount = dictionary[i]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = i
    print(f"Congratulations {winner}, you have won the auction with a bid of ${highest_bidder}!")
    print(congratulations)


auction = True

bids = {}

while auction:
    print(logo)

    print("Hello! Welcome to the auction\n")

    name = str(input("What is your name?\n"))

    amount = int(input("Please insert bid amount\n"))
    print("\n" * 100)
    final = str(input("Would you like to place another bid?\n")).lower()

    bids[name] = amount

    if final == "no":
        auction = False
        find_highest_bidder(bids)
    elif final == "yes":
        auction = True