import os
import stickman

current_try = 1
number_guesses = len(stickman.draw) - 1
final_guess_complete = False
final_guess = ""
alt_secret_word = ""

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
    for index in range(0, len(list_secret_word)):
        if (guess_letter.lower() == list_secret_word[index]) or (guess_letter.upper() == list_secret_word[index]):
            list_final_guess[index] = list_secret_word[index]
            list_secret_word[index] = " "
    final_guess = "".join(list_final_guess)
    alt_secret_word = "".join(list_secret_word)


def draw_hangman(current_try):
    print(stickman.draw[current_try])


def show_tries_left(number_guesses, current_try):
    if (number_guesses - current_try) == 0:
        print(f"This is your last chance!")
    else:
        print(f"Tries left: {number_guesses - (current_try - 1)}")


secret_word = input(
    "Type the secret word (Be careful with spaces): ")
os.system("cls")
list_secret_word = list(secret_word)
list_final_guess = [" "] * len(secret_word)
alt_secret_word = secret_word

while (current_try <= number_guesses) and (not final_guess_complete):
    draw_hangman(current_try - 1)
    show_tries_left(number_guesses, current_try)
    print(f"Secret word:")
    show_secret_word_w_underscores(list_final_guess)
    guess_letter = input("Try to guess one letter or try a complete word: ")
    if guess_letter == secret_word:
        show_secret_word_wo_underscores(guess_letter)
        print(
            f"Excellent the secret word is {guess_letter}, You won the challenge!")
        break
    elif len(guess_letter) > 1:
        os.system("cls")
        print(
            "You should enter just one character or the secret word, if you already guessed it.")
    elif (guess_letter.lower() in alt_secret_word) or (guess_letter.upper() in alt_secret_word):
        replace_user_coincidences(
            guess_letter, list_secret_word, list_final_guess)
        os.system("cls")
        print(f"The letter {guess_letter} is in the word. Well done!")
        if secret_word == final_guess:
            show_secret_word_wo_underscores(list_final_guess)
            final_guess_complete = True
            current_try = 6
            print(
                f"Excellent the correct word is {final_guess}, You won the challenge!")
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


"""
#2
When the word is a compound word, the program has to ignore them and just care about
of the real characters that compound the world E.g. "Hello World"
I don't have to introduce a " " character to complete the word. The word just has to include it
also these spaces have to appear in the secret word instead underscores.
This will give the user the hint that is a compound word. And probabilities to win increment.
"""
