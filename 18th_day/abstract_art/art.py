"""
A program that make some freak art based on colors of an image
The way to run this is just python main.py, you gonna need Python 3.13.2
"""

from turtle import *
import colorgram
import random
import sys

colors = colorgram.extract("itadori.jpg", 10)
color_list = []

for color in colors:
    color_list.append((color.rgb[0], color.rgb[1], color.rgb[2]))

# print(random.choice(color_list))

# sys.exit(0)

setup(width=600, height=400)
bgcolor("white")
title("This is my first turtle Program")
colormode(255)

# middle_of_screen =
# We can play with the window_width dimensions and also with the window_height
# -50
initial_x_pos = float(-((window_width()/2)-50))
final_x_pos = float(((window_width()/2)-50))
initial_y_pos = float(-((window_height()/2)-50))
final_y_pos = float(((window_height()/2)-50))

# Pen setup
# color("blue")
width(3)
speed("fastest")


def have_enough_space_x(x_pos):
    """Return True if the x coordinate is less or equal to the final x coordinate"""
    global final_x_pos
    return x_pos <= final_x_pos  # True if we have enough space in X


def have_enough_space_y(y_pos):
    global final_y_pos
    return y_pos <= final_y_pos  # True if we have enough space in Y


def print_init_and_final_pos():
    global initial_x_pos, initial_y_pos, final_x_pos, final_y_pos
    print(f"Initial position in x: {initial_x_pos}\n"
          f"Initial position in y: {initial_y_pos}\n"
          f"Final position in x: {final_x_pos}\n"
          f"Final position in y: {final_y_pos}\n")


penup()


x_pos = initial_x_pos
y_pos = initial_y_pos

print_init_and_final_pos()
# sys.exit(0)

while True:
    random_color = random.choice(color_list)
    # This will end the draw
    if not have_enough_space_y(y_pos):
        break
    elif have_enough_space_x(x_pos):
        goto((x_pos, y_pos))
        print(f"Current position: {pos()}")
        dot(20, random_color)
        x_pos += 50
        if not have_enough_space_x(x_pos):
            x_pos = initial_x_pos
            y_pos += 50


# This waits for the window closes
done()
