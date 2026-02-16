from drawable_pen import Drawable

d = Drawable()


def draw():
    d.draw_spirograph(25)


# d.draw_first_six_polygons()
d.s.listen()
d.s.onkey(key="s", fun=draw)
d.wait_to_close_window()

# Create a drawable that listen when I press "s" key and start the draw I indicate to the constructor
# at the creation moment
