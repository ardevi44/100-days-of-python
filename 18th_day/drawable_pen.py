from turtle import Turtle, Screen
import random


class Drawable:

    def __init__(self, distance: int = 10):
        """Initialize a Drawable object with its configuration"""
        self.set_initial_config()
        self.distance = distance
        self.movements = 100

    def set_initial_config(self):
        # Screen parameters
        self.s = Screen()
        self.s.colormode(255)
        # Pen parameters
        self.t = Turtle()
        self.t.speed("normal")
        self.t.width(5)

    def set_pen_color(self, random_color):
        self.t.color(random_color)

    def move_forward(self, distance: int):
        self.t.forward(distance)

    def move_right(self, distance: int):
        self.t.right(90)
        self.t.forward(distance)

    def move_left(self, distance: int):
        self.t.left(90)
        self.t.forward(distance)

    def move_backward(self, distance: int):
        self.t.backward(distance)

    def generate_random_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def wait_to_close_window(self):
        self.s.exitonclick()

    def make_random_movements(self, distance: int = 30):
        while self.movements > 0:
            self.set_pen_color(self.generate_random_color())
            match random.randint(1, 4):
                case 1:
                    self.move_forward(distance)
                case 2:
                    self.move_right(distance)
                case 3:
                    self.move_left(distance)
                case 4:
                    self.move_backward(distance)
            self.movements -= 1
        self.wait_to_close_window()

    def draw_a_square(self):
        side_length = 100
        self.t.color(self.generate_random_color())
        for _ in range(4):
            self.t.rt(90)
            self.t.fd(side_length)
        self.wait_to_close_window()

    def draw_first_six_polygons(self):
        side_length = 100
        polygons = 20
        sides = 3
        for polygon in range(polygons):
            self.t.color(self.generate_random_color())
            for side in range(sides):
                self.t.forward(side_length)
                self.t.rt(360 / sides)
            sides += 1
        self.wait_to_close_window()

    def draw_spirograph(self, circles):
        gap_size = 360 / circles
        circle_count = 0
        if circles >= 10:
            self.t.speed("fastest")
        for circle in range(circles):
            self.set_pen_color(self.generate_random_color())
            self.t.circle(100)
            self.t.setheading(self.t.heading() + gap_size)
            circle_count += 1
        print(f"Num circles: {circle_count}, Size of gap: {gap_size}")
        # Remember wait to close

    def draw_a_dashed_line(self):
        length = 10
        num_lines = 10
        # Initial state down
        for _ in range(num_lines * 2):
            self.t.forward(length)
            if self.t.isdown():
                self.t.penup()
            else:
                self.t.pendown()
        self.wait_to_close_window()
