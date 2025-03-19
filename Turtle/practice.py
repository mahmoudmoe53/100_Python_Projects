import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)


angle = 360

def random_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rbg = (r, b, g)
    return rbg


def draw_shape(num):
    for j in range(num):
        timmy.forward(100)
        timmy.right(360 / num)

shape = 3

for i in range(11):
    timmy.color(random_colour())
    draw_shape(shape)
    shape += 1



screen = Screen()

screen.exitonclick()