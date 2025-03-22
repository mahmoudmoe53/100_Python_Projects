from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score:{self.count}", align="center", font=("courier", 24, "normal"))
        self.hideturtle()

    def score(self):
        self.clear()
        self.count +=1
        self.write(arg=f"Score:{self.count}", align="center", font=("courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GameOver!!", align="center", font=("courier", 24, "normal"))



