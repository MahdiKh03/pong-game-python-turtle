from turtle import Screen, Turtle
from paddle import Paddles
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard


ball = Ball()

scoreboard = ScoreBoard()

screen = Screen()
screen.bgcolor("black")
screen.setup(1280, 720)
screen.title("Pong Game")
screen.listen()
screen.tracer(0)


paddles = Paddles()
# controlling the right paddle
screen.onkeypress(paddles.r_paddle_up, "Up")
screen.onkeypress(paddles.r_paddle_down, "Down")
# controlling the left paddle
screen.onkeypress(paddles.l_paddle_up, "w")
screen.onkeypress(paddles.l_paddle_down, "s")


def half_line():
    line = Turtle(shape="square")
    line.color("white")
    line.hideturtle()
    line.pensize(5)
    line.penup()
    line.goto(0, 360)
    line.setheading(270)

    for _ in range(72):
        line.pendown()
        line.forward(5)
        line.penup()
        line.forward(15)

    screen.update()


half_line()

while True:
    sleep(ball.ball_speed)
    screen.update()
    ball.move()
    ball.wall_reflection()
    ball.paddle_reflection(paddles.r_paddle)
    ball.paddle_reflection(paddles.l_paddle)
    if ball.xcor() > 610:
        scoreboard.l_point()
        ball_speed = 0.04
        ball.refresh_check()

    elif ball.xcor() < -610:
        scoreboard.r_point()
        ball.refresh_check()


