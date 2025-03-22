import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape(name="turtle")


def move_forward():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_right():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_left():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.home()
    timmy.clear()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")





screen.exitonclick()


