from turtle import Screen
from paddles import Paddles
import time
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect if it hit top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # detect when passes right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect when passes left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
