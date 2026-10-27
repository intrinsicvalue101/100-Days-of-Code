from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # TODO 1: Turn the animation off

# Initiate objects
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# paddle = Turtle() # TODO 2 : Create The paddle
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(r_paddle.go_up, "Up") # dont add function parenthesis when passing function in as parameter
screen.onkey(r_paddle.go_down, "Down") # dont add function parenthesis when passing function in as parameter
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on: # TODO 3: Update screen and show everything thats happened in background
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle and left_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()