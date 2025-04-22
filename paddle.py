from turtle import Turtle


class Paddles:
    def __init__(self):
        self.r_paddle = Turtle(shape="square")
        self.r_paddle.color("white")
        self.r_paddle.penup()
        self.r_paddle.goto(600, 0)
        self.r_paddle.shapesize(5, 1)

        self.l_paddle = Turtle(shape="square")
        self.l_paddle.color("white")
        self.l_paddle.penup()
        self.l_paddle.goto(-600, 0)
        self.l_paddle.shapesize(5, 1)

    def r_paddle_up(self):
        self.r_paddle.goto(self.r_paddle.xcor(), self.r_paddle.ycor() + 30)

    def r_paddle_down(self):
        self.r_paddle.goto(self.r_paddle.xcor(), self.r_paddle.ycor() - 30)

    def l_paddle_up(self):
        self.l_paddle.goto(self.l_paddle.xcor(), self.l_paddle.ycor() + 30)

    def l_paddle_down(self):
        self.l_paddle.goto(self.l_paddle.xcor(), self.l_paddle.ycor() - 30)
