import random

characters = [
    {
        "char_id": 1,
        "name": "Zombie Man",
        "power_level": 5,
    },
    {
        "char_id": 2,
        "name": "Genos, Demon Cyborg",
        "power_level": 7,
    },
    {
        "char_id": 3,
        "name": "Engine Knight",
        "power_level": 7,
    },
    {
        "char_id": 4,
        "name": "Fubuki",
        "power_level": 6,
    },
    {
        "char_id": 5,
        "name": "Sneck",
        "power_level": 4,
    },
    {
        "char_id": 6,
        "name": "Superalloy Darkshine",
        "power_level": 7,
    },
    {
        "char_id": 7,
        "name": "Death Gatling",
        "power_level": 5,
    },
    {
        "char_id": 8,
        "name": "Lightspeed Flash",
        "power_level": 8,
    },
    {
        "char_id": 9,
        "name": "Lightspeed Flash",
        "power_level": 8,
    }
]

score = 0
choice = ""
# This variable is the previous versus selected
previously_selected = []
game_ends = False
user_won_previous = False


# We're gonna get a random character from the list
def get_random_character(index):
    global characters
    character = characters[index]
    return character


print("""Welcome to the Higher Or Lower One Punch Man Game 👊
""")

# print(f"\nThese are the previous occurrences:")
# print(previously_selected)

while not game_ends:

    # 1. Select two character first
    if not user_won_previous:
        character_a = get_random_character(
            random.randint(0, len(characters) - 1))
    else:
        character_a = character_a
    character_b = get_random_character(random.randint(0, len(characters) - 1))

    # 2. Every time they are the same or they have the same power level we need to reselect one of them
    while character_a.get("char_id") == character_b.get("char_id") or character_a.get("power_level") == character_b.get("power_level"):
        character_b = get_random_character(
            random.randint(0, len(characters) - 1))

    # Pending ... Sorry about my English
    # The program is running well but we need to save the previous occurrences
    # this way we could check them so we could select different choices every time
    # while they're not in the list of occurrences, and remove one of the these
    # every 5 or 6 so this way we could show characters vs other characters with more
    # difference of time I think.
    previously_selected.append(
        f"{character_a.get("char_id")},{character_b.get("char_id")}")

    print(f"{character_a.get("name")} vs. {character_b.get("name")}")

    correct_answer = False
    while not correct_answer:
        choice = input(f"""
    Who do you think will win?

    'L' for {character_a.get("name")}
    'R' for {character_b.get("name")}

    Type your answer here ->: """).lower().strip()

        if choice == "l":
            correct_answer = True
            user_choice = character_a
            char_to_compare = character_b
        elif choice == "r":
            correct_answer = True
            user_choice = character_b
            char_to_compare = character_a
        else:
            print("Wrong choice")

    if user_choice.get("power_level") < char_to_compare.get("power_level"):
        print(f"""
    Score: {score}

    Sorry but You loose. Better luck next time.
    """)
        user_won_previous = False
        game_ends = True
    elif user_choice.get("power_level") > char_to_compare.get("power_level"):
        score += 1
        user_won_previous = True
        print(f"""
    Very Well this is your score: *** {score} ***
    """)
