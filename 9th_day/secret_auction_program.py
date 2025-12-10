import os


def check_for_more_bidders(more_bidders, bids):
    """Take an string 'yes'|'no' and a dictionary of bids, and clean the console if there are more bidders
    and decides the winner if are not"""
    if more_bidders == "yes":
        os.system("cls")
        return True
    else:
        os.system("cls")
        say_winner(bids)
        return False


def say_winner(bids):
    """Take the bids and decides which user has won, based on its bids"""
    greater_bid = 0
    name = ""
    winner = {}
    for user, bid in bids.items():
        if bid > greater_bid:
            greater_bid = bid
            name = user
            winner = {user: greater_bid}
    winner_bid = "{:.2f}".format(winner[name])
    print(
        f"The winner is {name} with a bit of ${winner_bid}")


more_bidders = True
bids = {}

print("Welcome to the secret auction program.")

while (more_bidders):
    user_name = input("What's your name?: ").lower().strip()
    bid = float(input("What's your bid?: $"))
    bids[user_name] = bid
    are_more_bidders = input(
        "Are there any other bidders? Type \"yes\" or \"no\": ").lower().strip()
    more_bidders = check_for_more_bidders(are_more_bidders, bids)
