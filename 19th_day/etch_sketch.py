# This is a small Etch an Sketch application
from turtle import Turtle, Screen
from random import randint


class EtchSketch:
    def __init__(self):
        self.s = Screen()
        self.t = Turtle()
        self.s.colormode(255)
        self.canvas = self.s.getcanvas()
        self.t.width(5)
        self.t.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.t.speed("fastest")

    def check_key_pressed(self):
        def report_key(event):
            print(f"You're pressing: {event.keysym}")

        self.canvas.bind("<Key>", report_key)

    def draw(self):
        def get_direction(event):
            match event.keysym:
                case "w" | "Up":
                    self.t.forward(10)
                case "s" | "Down":
                    self.t.backward(10)
                case "a" | "Left":
                    # Counter-clockwise
                    self.t.left(10)
                case "d" | "Right":
                    self.t.right(10)
                case "c":
                    self.t.clear()
                    self.t.up()
                    self.t.home()
                    self.t.down()
                    self.t.left(90)

        self.canvas.bind("<Key>", get_direction)

    def prevent_close_window(self):
        self.s.listen()
        self.s.mainloop()


# canvas.bind("<Key>", move)
sketch_1 = EtchSketch()
# sketch_1.check_key_pressed()
sketch_1.draw()
sketch_1.prevent_close_window()
