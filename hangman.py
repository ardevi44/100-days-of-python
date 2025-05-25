# This file contents the solution of the course for the hangman challenge
# Angela's solution actually
import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["aardvark", "baboon", "camel"]

# choose a random word from the list and print it with its length
chosen_word = random.choice(word_list)
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
    # ask the user for a letter ...
    guess = input("Guess a letter: ").lower()
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
    if "_" not in display:
        game_over = True
        print("You win!")
