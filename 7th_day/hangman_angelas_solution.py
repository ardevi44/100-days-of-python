# This file contents the solution of the course for the hangman challenge
# Angela's solution actually
import random
import hangman_words
# another way to do as above
# from hangman_words import word_list
from hangman_words import logo
# import os

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
"""
]

lives = 6
print(logo)

# choose a random word from the list and print it with its length
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
print(f"length {len(chosen_word)}")

# NOTE: remember the range function with just one parameter will make a loop of "that parameter" times beginning at 0

# Takes the placeholder and fill it with underscores as much the chosen word has letters ...
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've al ready guessed {guess}")
    # ask the user for a letter ...
    print(
        f"******************************{lives}/6 LIVES LEFT******************************")
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        elif letter == guess:
            display += letter
            correct_letters.append(letter)
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guessed {guess}, that's not in the word. You loose a life.")
        if lives == 0:
            game_over = True
            print(
                f"******************************IT WAS {chosen_word}! YOU LOOSE******************************")
    if "_" not in display:
        game_over = True
        print(f"******************************YOU WIN!******************************")
    print(stages[lives])
