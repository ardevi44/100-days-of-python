from turtle import *

forward(100)
left(120)
forward(100)
up()
home()
left(180-120)
down()
forward(100)
up()
home()

down()

color("red")
fillcolor("yellow")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

exitonclick()
