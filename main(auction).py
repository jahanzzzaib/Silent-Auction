print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______|_'-''"---------''-'_'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to The Silent Auction!")
bids = {}
bidding_over = False


def find_highest_bidder(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}!")


while not bidding_over:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $ "))
    print("\n")
    bids[name] = bid
    restart = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if restart == "yes":
        print("\n" * 100)
    elif restart == "no":
        bidding_over = True
        find_highest_bidder(bids)
