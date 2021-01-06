from turtle import Turtle

STEP = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)


    def up(self):
        if self.ycor() > 230:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() < -230:
            pass
        else:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)

