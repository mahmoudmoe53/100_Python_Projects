import turtle
from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
user_bet = turtle.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

colours =["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_positions = [-70, -40, -10, 20, 50, 80]
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)
        if i.xcor() > 230:
            winning_colour = i.pencolor()
            is_race_on = False
            if winning_colour == user_bet:
                print(f"You've won!! The winning turtle was {winning_colour}")
            else:
                print(f"You've lost. The winning turtle was {winning_colour}")










screen.exitonclick()