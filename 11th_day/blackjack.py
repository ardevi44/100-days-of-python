from game_functions import *
print("Shuffling...")
np.random.shuffle(copy_deck)

show_money_status()
ask_for_bets()
deal_cards()
choose_option()
