# import random
import os

current_try = 1
number_guesses = 5
final_guess_complete = False
final_guess = ""
alt_secret_word = ""

# Ask the secret word
secret_word = input(
    "Type the secret word (Be careful with spaces): ")
os.system('cls')

# pass the secret word to a list.
list_secret_word = list(secret_word)
# Create an empty list with the same length of the secret word list
list_final_guess = [" "] * len(secret_word)
# alternative secret word, prevent mutated the original
alt_secret_word = secret_word

# Print the current final guessed word with underscores


def show_secret_word_w_underscores(list_final_guess):
    for blank in list_final_guess:
        if blank == " ":
            print(f"_ ", end="")
        else:
            print(f"{blank} ", end="")
    print()

# Print the current final guessed word without underscores


def show_secret_word_wo_underscores(list_final_guess):
    for letter in list_final_guess:
        if letter == "_":
            print(f"  ", end="")
        else:
            print(f"{letter} ", end="")
    print()


def replace_user_coincidences(guess_letter, list_secret_word, list_final_guess):
    index = 0
    # This loop will put into the result word all the coincidences of the guess
    for index in range(0, len(list_secret_word)):
        if (guess_letter.lower() == list_secret_word[index]) or (guess_letter.upper() == list_secret_word[index]):
            list_final_guess[index] = list_secret_word[index]
            list_secret_word[index] = " "
    # End this for loop

    # take the result word if it was updated and the secret word left
    final_guess = "".join(list_final_guess)
    alt_secret_word = "".join(list_secret_word)


def show_tries_left(guesses, current_try):
    if (guesses - current_try) == 0:
        print(f"Last chance")
    else:
        print(f"Tries left: {guesses - (current_try - 1)}")


while (current_try <= number_guesses) and (not final_guess_complete):
    show_tries_left(number_guesses, current_try)
    print(f"Secret word:")
    show_secret_word_w_underscores(list_final_guess)
    guess_letter = input("Try to guess one letter or try a complete word: ")
    if guess_letter == secret_word:  # If the guess is the secret word
        show_secret_word_wo_underscores(guess_letter)
        print(
            f"Excellent the secret word is {guess_letter}, You won the challenge!")
        break
    elif len(guess_letter) > 1:  # If the length of the guess is greater than just one character
        print(
            "You should enter just one character or the secret word, if you already guessed it.")
     # If the letter is in the secret word
    elif (guess_letter.lower() in alt_secret_word) or (guess_letter.upper() in alt_secret_word):
        replace_user_coincidences(
            guess_letter, list_secret_word, list_final_guess)
        if secret_word == final_guess:  # If the user finally found the word
            show_secret_word_wo_underscores(list_final_guess)
            # Break the loop
            final_guess_complete = True
            current_try = 6
            print(
                f"Excellent the correct word is {final_guess}, You won the challenge!")
            print("You won the game!")
            break
    elif current_try == number_guesses:  # The user ends his tries
        print("Sorry")
        print("You've lose the game")
        break
    else:  # The user still have chances but he fail the current try
        tries_left = number_guesses - current_try
        current_try += 1
        if tries_left == 0:
            print("You're in your last chance, Good luck, don't give up!")
        else:
            print("You've lost one try. Be careful")
        # TODO: draw a part of the stick man
