import os

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


bid_continue = True
bidders = {}
while bid_continue:
    os.system('clear')
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid

    another_bid = input("Are there any other bidders? Type 'yes or 'no': ")

    if another_bid == 'no':
        os.system('clear')
        bid_continue = False

highest_bid = 0
highest_bidder = ''
for bidder, bid in bidders.items():
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder

# highest_bid = max(list(bidders.keys()))
# print(highest_bid)
# print(list(bidders.values()))
# highest_bidder = (list(bidders.values())).index(highest_bid)
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")