import random

secret_number = random.randint(1, 100)
correct_op = False
attempts_numb = 10
game_ends = False

print("""
Welcome to the Number Guessing Game!  
I'm thinking of a number between 1 and 100
""")


while not correct_op:
    difficulty_op = input("""
Choose a difficulty. Type 'easy' or 'hard': """)
    if difficulty_op == "easy":
        correct_op = True
    elif difficulty_op == "hard":
        attempts_numb = 5
        correct_op = True

print(f"""
You have {attempts_numb} remaining to guess the number.
""")


while not game_ends:
    guessed_number = int(input("\nMake a guess: "))

    if guessed_number == secret_number:
        print(
            f"\nYou got it with {attempts_numb} attempts remaining. The number was {guessed_number}")
        game_ends = True
        break

    if guessed_number > secret_number:
        print(f"\nToo High.")
        attempts_numb -= 1
    elif guessed_number < secret_number:
        print("\nToo Low.")
        attempts_numb -= 1

    if attempts_numb == 0:
        print(f"\nAttempts: {attempts_numb}")
        print(
            f"Your attempts are done! You don't got it :(\nSe you in the next game.")
        break

    print(f"You have {attempts_numb} attempts remaining to guess the number!")
