from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move()
        self.bounce_x()

    def speed_up(self):
        self.move_speed /= 10


