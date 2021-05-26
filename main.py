from turtle  import Turtle
from  turtle import Screen
screen = Screen()
screen.colormode(255)

import random

timmy = Turtle()
import colorgram

colors = [(226, 31, 39), (3, 2, 2), (52, 113, 87), (164, 140, 123), (5, 98, 51), (222, 30, 38), (108, 83, 76), (223, 221, 219), (16, 50, 28), (47, 171, 101), (200, 221, 198), (2, 2, 5), (9, 3, 6), (224, 215, 219), (222, 54, 50), (137, 178, 147), (218, 220, 225), (173, 209, 168), (228, 172, 163), (192, 142, 146), (113, 42, 36), (172, 27, 35), (207, 195, 162), (164, 128, 82), (158, 159, 162), (84, 93, 96), (230, 169, 173), (76, 67, 44), (64, 62, 68), (125, 124, 134)]
r= random.choice(colors)
x_spot = -315 #X coordinates
y_spot = -200 #Y coordinates

for _ in range(10):
    timmy.penup()
    timmy.setx(x_spot)
    timmy.sety(y_spot)
    for _ in range(10):
        r = random.choice(colors)
        timmy.speed("fastest")
        timmy.color(r)
        timmy.begin_fill()
        timmy.circle(10,360)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(70)
        y_spot +=5















screen.exitonclick()