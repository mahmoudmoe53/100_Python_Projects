import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()

turtle.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")


def random_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rbg = (r, b, g)
    return rbg

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_colour())
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)
        timmy.circle(100)


draw_spirograph(5)



screen = Screen()

screen.exitonclick()