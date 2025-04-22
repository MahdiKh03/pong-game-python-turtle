from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xcor_move = 10
        self.ycor_move = 10
        self.ball_speed = 0.04

    def move(self):
        self.goto(self.xcor() + self.xcor_move, self.ycor() + self.ycor_move)

    def wall_reflection(self):
        if self.ycor() > 340 or self.ycor() < -340:
            self.ycor_move *= -1

    def paddle_reflection(self, paddle):
        if self.xcor() > 580 and self.distance(paddle) < 50 or self.xcor() < -580 and self.distance(paddle) < 50:
            self.xcor_move *= -1
            self.ball_speed *= 0.75

    def refresh_check(self):
        self.goto(0, 0)
        self.ball_speed = 0.04
        sleep(1.5)
        self.ycor_move *= -1
        self.xcor_move *= -1




