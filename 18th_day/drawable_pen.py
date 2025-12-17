from turtle import Turtle
from turtle import Screen
import random


class Drawable:

    def __init__(self, distance: int = 10):
        """Initialize a Drawable object with its configuration"""
        self.s = Screen()
        self.s.colormode(255)
        self.t = Turtle()
        self.t.width(5)
        self.distance = distance
        self.movements = 100
        self.colors = [(35, 23, 206), (206, 23, 23),
                       (194, 206, 23), (206, 23, 197)]

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

    def generate_random_movements(self, distance: int = 30):
        i = 0
        while self.movements > 0:
            i = 0 if i == len(self.colors) else i
            tuple_color = self.colors[i]
            self.t.color(tuple_color)
            number_movement = random.randint(1, 4)
            match number_movement:
                case 1:
                    self.move_forward(distance)
                case 2:
                    self.move_right(distance)
                case 3:
                    self.move_left(distance)
                case 4:
                    self.move_backward(distance)
            i += 1
            self.movements -= 1
        self.s.exitonclick()
