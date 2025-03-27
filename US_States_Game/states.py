from turtle import Turtle

class States(Turtle):
    def __init__(self, state_name, x_cor, y_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.goto(self.x_cor, self.y_cor)
        self.state = state_name

    def write_name_of_state(self):
        """This is a function that adds the guessed state to the map"""
        self.write(self.state)
