from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_change = 10
        self.x_change = 10
        self.setheading(random.randint(1, 360))
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_change *= -1

    def hit(self):
        self.x_change *= -1
        self.move_speed *= 0.9 #Move speed increases each time the ball is hit

    def reset_pos(self, turn):
        self.goto(x=0, y=0)
        self.move_speed = 0.1

        if turn % 2 == 0:
            self.y_change = -10
            self.x_change = -10
        else:
            self.y_change = 10
            self.x_change = 10
