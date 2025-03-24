from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=260)
        self.level = 1
        self.update_score_board()



    def update_score_board(self):
        self.color("white")
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def add_score(self):
        self.level += 1
        self.update_score_board()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(x=-0, y=0)
        self.write("GAMEOVER!", align="center", font=FONT)




