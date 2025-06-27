# This will contain the main program "Tha BlackJack Game"
import numpy as np
# Global variables
from cards_deck import cards_deck as deck
player_money = 2500
player_bet = 0
player_cards = []
player_score_cards = 0
software_money = 2500
software_bet = 0
software_cards = []
software_score_cards = 0
# Copy the deck array, for not update the original
copy_deck = np.array(deck).copy()


def ask_for_bets():
    global player_bet
    global software_bet
    global player_money
    global software_money

    player_bet = float(input("Place your bet: "))
    software_bet = player_bet

    player_money -= player_bet
    software_money -= software_bet
    show_money_status()


def show_money_status():
    global player_money
    global software_money
    print(f"Player money: {player_money}")
    print(f"Software money: {software_money}")


"""
def print_one_card(card):
    card_it = zip(card)
    for row in card_it:
        print(row)
"""

"""
def print_two_cards(cards_array):
    # Remember to use the split function in each string
    cards_pair = zip(
        cards_array[0]["ascii_art"].split("\n"),
        cards_array[1]["ascii_art"].split("\n"))
    for row in cards_pair:
        print(row[0], row[1])
"""


def print_player_score():
    global player_score_cards
    print(f"Player score: {player_score_cards}")


def print_dealer_score():
    global software_score_cards
    print(f"Dealer score: {software_score_cards}")


def is_ace(card, current_score):
    if "is_ace" in card:
        value = 11
        if (current_score + value) > 21:
            value = 1
        card["value"] = value
    return card


def sum_score(card, turn):
    global player_score_cards
    global software_score_cards
    if turn == "player":
        card = is_ace(card, player_score_cards)
        player_score_cards += card["value"]
    else:
        card = is_ace(card, software_score_cards)
        software_score_cards += card["value"]


def show_players_cards(player_cards, software_cards):
    print("Player cards: ")
    # Print player's cards ...
    for index, card in enumerate(player_cards):
        sum_score(card, turn="player")
        print(f"{index + 1} -> {card["code_card"]}")
    print_player_score()
    # Print dealers's cards ...
    print("Dealer cards: ")
    for index, card in enumerate(software_cards):
        if "hidden" in card:
            # sum_score(card, turn="dealer")
            print(f"{index + 1} -> hidden")
            # print(f"Card code: {card["code_card"]}")
            # print(f"Card value: {card["value"]}")
        else:
            sum_score(card, turn="dealer")
            print(f"{index + 1} -> {card["code_card"]}")
    print_dealer_score()


def deal_initial_cards():
    global player_cards
    global software_cards
    global copy_deck
    player_turn = True
    cards_to_deal = 2
    while (len(player_cards) < cards_to_deal) or (len(software_cards) < cards_to_deal):
        if player_turn:
            player_cards.append(copy_deck[-1])
            player_turn = False
        else:
            software_cards.append(copy_deck[-1])
            if len(software_cards) == 1:
                software_cards[-1]["hidden"] = True
            player_turn = True
        copy_deck = np.delete(copy_deck, -1)
    show_players_cards(player_cards, software_cards)


"""
def print_deck(deck):
    for index, card in enumerate(deck):
        ace_string = ""
        if "is_ace" in card:
            ace_value = "still unknown"
            ace_string = f" -> {ace_value}"
        print(
            f"{index+1} -> {card["name_card"]} -> {card["code_card"]}{ace_string}")
"""

"""
# This will be uncomment later
# Shuffle the copy deck
print("Shuffling...")
np.random.shuffle(copy_deck)
"""

# copy_deck = np.delete(copy_deck, -1)
"""
# This will be uncomment later
# Main execute of the program
show_money_status()
ask_for_bets()
deal_initial_cards()
"""

print(f"Length of the original deck: {len(deck)}")
