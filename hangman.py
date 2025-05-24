# This file contents the solution of the course for the hangman challenge
# Angela's solution actually
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
print(f"word length {len(chosen_word)}")

# NOTE: remember the range function with just one parameter will make a loop of "that parameter" times beginning at 0
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:
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
