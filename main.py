from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=int(600), width=int(800))
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard((0, -280))


screen.listen()
screen.onkeypress(r_paddle.up, "Up")  # Up arrow
screen.onkeypress(r_paddle.down, "Down")  # Down arrow
screen.onkeypress(l_paddle.up, "w")  # Up arrow
screen.onkeypress(l_paddle.down, "s")  # Down arrow

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

#Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

#Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.hit()

#Detect if ball goes out of the edge
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 0:
            scoreboard.increase_l()
        else:
            scoreboard.increase_r()
        ball.reset_pos(scoreboard.turn)



screen.exitonclick()