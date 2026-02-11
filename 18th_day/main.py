# from turtle import Turtle, Screen
# from turtle import Turtle as t
# from turtle import Screen as s
# from turtle import *
from drawable_pen import Drawable
from turtle import Turtle, Screen
import random


def draw_a_square(t_object, side_width):
    t_object.shape("turtle")
    t_object.color("red")
    for side in range(4):
        t_object.rt(90)
        t_object.fd(side_width)


def draw_a_dashed_line(t, length, num_lines):
    pen_is_down = True
    for i in range(num_lines * 2):
        if pen_is_down:
            t.forward(length)
            pen_is_down = False
        else:
            t.penup()
            t.forward(length)
            t.pendown()
            pen_is_down = True


def print_pentagon(turtle, side_len):
    """
    Draws a simple pentagon with side_len specification.

    Args:
      turtle (Turtle): A Turtle Object
      side_len (int): The desired length of the sides
    Returns:
      ---
    """
    angle = 360 / 5
    for i in range(5):
        turtle.forward(side_len)
        turtle.right(angle)


def print_first_six_polygons(t, side_len):
    polygons_number = 6
    sides_number = 3
    for i in range(polygons_number):
        for i in range(sides_number):
            degrees = 360 / sides_number
            t.forward(side_len)
            t.rt(degrees)
        sides_number += 1


# d = Drawable()
# d.generate_random_movements()
s = Screen()
s.colormode(255)
t = Turtle()
t.width(3)
t.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(15)

s.exitonclick()

"""
It is another solution

space_available = 360
angle_required = 5
number_of_circles = (space_available / angle_required)
while number_of_circles > 0:
    t.color(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    t.circle(100)
    t.left(angle_required)
    number_of_circles -= 1
"""
