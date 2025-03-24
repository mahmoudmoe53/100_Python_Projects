from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.penup()
        self.goto(position)


    def go_up(self):
        """ This function moves the paddle up"""
        new = self.ycor() + 20
        self.goto(x=self.xcor(), y=new)



    def go_down(self):
        """ This function moves the paddle down"""
        new = self.ycor() - 20
        self.goto(x=self.xcor(), y=new)



