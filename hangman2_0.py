import os
import stickman

current_try = 1
number_guesses = len(stickman.draw) - 1
final_guess_complete = False
final_guess = ""
alt_secret_word = ""

# Print the current final guessed word with underscores


def show_secret_word_w_underscores(list_final_guess, alt_secret_word):
    i = 0
    for i in range(len(list_final_guess)):
        if (alt_secret_word[i] == " ") and (list_final_guess[i] == " "):
            print("  ", end="")
        elif list_final_guess[i] == " ":
            print("_ ", end="")
        else:
            print(f"{list_final_guess[i]} ", end="")
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
    for index in range(0, len(list_secret_word)):
        if (guess_letter == list_secret_word[index]):
            list_final_guess[index] = list_secret_word[index]
            list_secret_word[index] = " "


def draw_hangman(current_try):
    print(stickman.draw[current_try])


def show_tries_left(number_guesses, current_try):
    if (number_guesses - current_try) == 0:
        print(f"This is your last chance!")
    else:
        print(f"Tries left: {number_guesses - (current_try - 1)}")


def show_secret_word_w_spaces(secret_word):
    print("\n")
    for letter in secret_word:
        print(f"{letter} ", end="")
    print("\n")


def hide_secret_word(list_secret_word):
    for letter in list_secret_word:
        if letter != " ":
            print(f"_ ", end="")
        else:
            print(f"  ", end="")
    print()


secret_word = input(
    "Type the secret word: ")
alt_secret_word = secret_word.lower().strip()
list_secret_word = list(alt_secret_word)
list_final_guess = [" "] * len(secret_word)
os.system("cls")
first_time = True

while (current_try <= number_guesses) and (not final_guess_complete):
    draw_hangman(current_try - 1)
    show_tries_left(number_guesses, current_try)
    print(f"Secret word:")
    if first_time:
        hide_secret_word(list_secret_word)
    else:
        show_secret_word_w_underscores(list_final_guess, alt_secret_word)
    first_time = False
    guess_letter = input(
        "Try to guess one letter or try a complete word: ").lower().strip()
    if guess_letter == "":
        os.system("cls")
        print("At least one character")
        continue
    if guess_letter == alt_secret_word:
        show_secret_word_w_spaces(secret_word)
        print(
            f"Excellent the secret word is -> {secret_word} <-, You won the challenge!")
        break
    elif len(guess_letter) > 1:
        os.system("cls")
        print(
            "Enter just one character or the secret word, if you already guessed it. Try again")
    elif (guess_letter in alt_secret_word):
        replace_user_coincidences(
            guess_letter, list_secret_word, list_final_guess)
        final_guess = "".join(list_final_guess)
        os.system("cls")
        print(f"The letter {guess_letter} is in the word. Well done!")
        if alt_secret_word == final_guess:
            draw_hangman(current_try - 1)
            show_secret_word_wo_underscores(list_final_guess)
            final_guess_complete = True
            current_try = 6
            print(
                f"Excellent the correct word is {secret_word}, You won the challenge!")
            print("You won the game!")
            break
    elif current_try == number_guesses:
        os.system("cls")
        print("Sorry")
        print("You've lose the game")
        draw_hangman(current_try)
        print(f"The secret word was: {secret_word}")
        break
    else:
        tries_left = number_guesses - current_try
        current_try += 1
        os.system("cls")
        if tries_left == 0:
            print("You're in your last chance, Good luck, don't give up!")
        else:
            print("You've lost one try. Be careful")
