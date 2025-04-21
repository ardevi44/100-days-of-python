import random

rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_ascii = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [
    ["rock", rock_ascii],
    ["paper", paper_ascii],
    ["scissors", scissors_ascii]
]
user_choice = ""

print("Hello welcome to the rock, paper, scissors game!")
print("You'll play against the computer.")

comp_choice = options[random.randint(0, 2)]

choice = input("""
type an option:
[r] -> rock
[p] -> paper
[s] -> scissors

-> """).lower()


if choice == "r":
    user_choice = options[0]
elif choice == "p":
    user_choice = options[1]
elif choice == "s":
    user_choice = options[2]
else:
    user_choice = "IC"

if user_choice == "IC":
    print("Invalid character. Exit.")
else:
    print(f"""
  User choice
  {user_choice[0]}
  {user_choice[1]}
  Computer choice
  {comp_choice[0]}
  {comp_choice[1]}
  """)

    # User wins possibilities
    draw = user_choice[0] == comp_choice[0]
    rock_v_scissors = user_choice[0] == options[0][0] and comp_choice[0] == options[2][0]
    scissors_v_paper = user_choice[0] == options[2][0] and comp_choice[0] == options[1][0]
    paper_v_rock = user_choice[0] == options[1][0] and comp_choice[0] == options[0][0]

    if draw:
        print("You're actually in a draw")
    elif rock_v_scissors or scissors_v_paper or paper_v_rock:
        print("**Congratulations you win!**")
    else:
        print("++Sorry, Computer wins!++")
