# Is moment of taking decisions
# This script will be the sample of using if else statements in my python code ...
# --------------------------------------------------------------------------------

# The statement sample looks like this

# if condition:
#  do this
# else:
#  do this

# Indentation is important in python

# Check if a person can ride on the roller coaster
# -------------------------------------------------

# bill = 0
# print("Welcome to the rollercoaster!")
# height = float(input("What's your height in cm? "))
# height = 172

# if height >= 120:
# print(f"You can ride the rollercoaster!")
# age = 18
# age = int(input("How old are you? "))
#     if age <= 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     else:
#         bill = 12
#     print(f"You should pay: ${bill:.2f} ")
#     wants_photo = input(
#         "Do you want to have a photo take? Type [y] for Yes and [n] for No: ")
#     if wants_photo == "y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# taking decisions using math

# Check if a number is odd or even
# --------------------------------
# number = -2
# if number % 2 == 0:
#     print(f"{number} is Even.")
# else:
#     print(f"{number} is Odd.")


# BMI calculator mini project
# ---------------------------

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi < 18.5:
#     print("underweight")
# elif bmi < 25:
#     print("normal weight")
# else:
#     print("overweight")

# Pizza delivery program
# ----------------------

# TODO: work out how much they need to pay based on their size choice.

# TODO: work out how much to add to their bill based on their pepperoni choice.

# TODO: work out their final amount based on whether if they want extra cheese.

bill = 0
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()

if size == "s":
    bill = 100
elif size == "m":
    bill = 150
elif size == "l":
    bill = 170
else:
    print("You should select a correct size. See you next time")

if bill != 0:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if pepperoni == "y":
        bill += 20
    if extra_cheese == "y":
        bill += 15
    print(f"Thanks for shopping with us. Your total bill is ${bill:.2f}")
bill = float(bill)
