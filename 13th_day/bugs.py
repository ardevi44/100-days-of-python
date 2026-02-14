# Some examples to debug, don't pay attention on this
from random import randint


def roll_a_dice():
    dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = randint(0, 5)
    print(dice_images[dice_num])


def check_millennial_or_gen_z():
    year = int(input("What's your birth year? "))
    if year > 1980 and year < 1994:
        print("You're a millennial")
    elif year >= 1994:
        print("You're a Gen Z")


def check_driver_license():
    while True:
        try:
            age = int(input("Write your numerical age, like 23: "))
            break
        except ValueError:
            print("Something wrong. You should input a numerical value, such as 23 or 15")

    if age >= 18:
        print("You can drive")
    else:
        print("You shouldn't drive right now")


check_driver_license()
