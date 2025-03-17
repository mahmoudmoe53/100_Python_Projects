from turtle import Turtle, Screen
from prettytable import PrettyTable




table = PrettyTable()

table.align = "c"
table.add_column("Pokemon",["Abra", "Garchomp", "Celebi"])
table.add_column("Type", ["Psychic", "Dragon", "Grass/Psychic"])
print(table)


timmy = Turtle()

timmy.color("cyan")
timmy.shape("turtle")
timmy.forward(100)

my_screen = Screen()

print(my_screen.canvheight)

my_screen.exitonclick()


