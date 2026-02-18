from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)
is_race_on = False


def generate_colored_turtles():
    turtle_box = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for turtle_color in colors:
        t = Turtle(shape="turtle")
        t.color(turtle_color)
        t.up()
        turtle_box.append(t)
    return turtle_box


def send_turtles_start(turtle_rainbow):
    s_width = screen.window_width()
    s_height = screen.window_height()
    # Setting the width starter position
    _95_percent = 0.90 * s_width
    start_x_pos = _95_percent / 2
    start_x_pos = -1 * (start_x_pos)
    # Setting the height starter position
    _70_percent = 0.70 * s_height
    start_y_pos = _70_percent / 2
    space = _70_percent / len(turtle_rainbow)
    # don't need negative
    for turtle in turtle_rainbow:
        turtle.goto(start_x_pos, start_y_pos)
        start_y_pos -= space


turtle_rainbow = generate_colored_turtles()
send_turtles_start(turtle_rainbow)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle you think will win the race?"
    "\nEnter a color: "
)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_rainbow:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} is the winner!")
        turtle.forward(randint(1, 10))


screen.mainloop()
