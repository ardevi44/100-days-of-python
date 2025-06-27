from game_functions import *
# Shuffle the copy deck
print("Shuffling...")
np.random.shuffle(copy_deck)

show_money_status()
ask_for_bets()
deal_initial_cards()
