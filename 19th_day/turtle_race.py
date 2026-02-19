from turtle import Turtle, Screen
from random import randint
from tkinter import messagebox


screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def generate_colored_turtles():
    turtle_box = []
    # colors = ["red", "orange", "yellow", "green", "blue", "purple"]
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


included_color = False
wrong_color_msg = ""
while not included_color:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt=f"{wrong_color_msg}" +
        "Which turtle you think will win the race?"
        "\nEnter a color: "
    )
    if not user_bet:
        break
    for color in colors:
        if user_bet == color:
            included_color = True
            break
    wrong_color_msg = "Color not included!\n"


winning_turtle = ""
race_over = False
if user_bet:
    while True:
        for turtle in turtle_rainbow:
            turtle.forward(randint(1, 10))
            if turtle.xcor() > 230:
                winning_turtle = turtle.pencolor()
                race_over = True
                break
        if race_over:
            break
    if winning_turtle == user_bet:
        messagebox.showinfo(
            message=f"You've won! The {winning_turtle} is the winner!")
    else:
        messagebox.showinfo(
            message=f"You've lost! The {winning_turtle} is the winner!")
else:
    messagebox.showinfo(message="You didn't bet. See the next one")
    screen.bye()


# screen.mainloop()
