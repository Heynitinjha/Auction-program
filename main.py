logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bid = {}
Play = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for biding in bidding_record:
        bidgame = bidding_record[biding]
        if bidgame > highest_bid:
            highest_bid = bidgame
            winner = biding
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not Play:
    Name = input("Enter the name :")
    Amount = int(input("Enter the amount:"))
    bid[Name] = Amount
    Should_continue = input("is there any other bid ? please type yes or no")
    if Should_continue == "no":
        Play = True
        find_highest_bidder(bid)
    elif Should_continue == "yes":
        continue

