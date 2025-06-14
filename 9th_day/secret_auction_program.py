import os


def check_for_more_bidders(bidders, user_bids):
    if bidders == "yes":
        os.system("cls")
        return True
    else:
        os.system("cls")
        say_winner(user_bids)
        return False


def say_winner(user_bids):
    max = 0
    winner = {}
    for user in user_bids:
        if user_bids[user] > max:
            max = user_bids[user]
            winner[user] = user
            winner[bid] = user_bids[user]

    winner_bid_f = "{:.2f}".format(winner[bid])
    print(
        f"The winner is {winner[user].capitalize()} with a bit of ${winner_bid_f}")


more_bidders = True
user_bids = {}

print("Welcome to the secret auction program.")

while (more_bidders):
    user_name = input("What's your name?: ").lower().strip()
    bid = float(input("What's your bid?: $"))
    user_bids[user_name] = bid
    bidders = input(
        "Are there any other bidders? Type \"yes\" or \"no\": ").lower().strip()
    more_bidders = check_for_more_bidders(bidders, user_bids)
