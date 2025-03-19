import turtle as turtle_module
import random

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

colour_list = [(229, 228, 226), (225, 223, 224), (199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35), (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53), (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152), (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171), (169, 200, 209), (205, 183, 188), (41, 75, 61), (148, 116, 122), (39, 72, 81), (97, 138, 153)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

numb_dots = 100

for dot_count in range(1, numb_dots + 1):
    timmy.dot(20, random.choice(colour_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()

screen.exitonclick()