from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open(file="data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.count} Highscore: {self.high_score}", align="center", font=("courier", 24, "normal"))



    def update_highscore(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.count = 0
        self.update_scoreboard()



    def score(self):
        self.count +=1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.update_scoreboard()


