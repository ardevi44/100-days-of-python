# This file contents the solution of the course for the hangman challenge
# Angela's solution actually
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)
print(f"word length {len(chosen_word)}")

# TODO-4 - Create a placeholder with the same number of blanks as the chosen_word
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
    # Change the for loop so that you keep the previous correct letters in display
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

# At this point angela is using two string variables to solve the problem, very lightweight solution.
