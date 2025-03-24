from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
score = ScoreBoard()

screen.tracer(0)
screen.bgcolor("black")
screen.title("Mahmoud's Pong Game")
screen.setup(width=800, height=600)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

ball = Ball()

screen.listen()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        score.l_point()
        ball.restart()

    if ball.xcor() < -380:
        score.r_point()
        ball.restart()










screen.exitonclick()