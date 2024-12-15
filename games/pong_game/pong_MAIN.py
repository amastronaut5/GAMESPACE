import random
#create a screen
from turtle import Screen,Turtle
import time
import ball
from pongscoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.setup(850,600,)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)

scoreboard = Scoreboard()



r_paddle = Paddle((390,0))
l_paddle = Paddle((-390,0))
ball = Ball()




b = Turtle()
b.penup()
b.hideturtle()
b.pencolor("white")






# for _ in range(14):
# while divider.ycor() != -400:
#     divider.pendown()
#     divider.forward(20)
#     divider.penup()
#     divider.forward(20)
#     divider.pendown()
#     divider.dot()
#     divider.penup()
#     divider.forward(20)
#
#
# #
# def border():
#     b.goto(-400, 300)
#     b.pendown()
#     b.goto(400, 300)
#     b.goto(400, -300)
#     b.goto(-400, -300)
#     b.goto(-400, 300)
#
#
#


game_is_on=True
while game_is_on:
    screen.listen()
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")
    # border()
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with the paddle

    if ball.distance(r_paddle)<50 and ball.xcor() >350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350 :
        ball.bounce_x()



    if ball.xcor()>390:
        ball.reset()
        ball.bounce_x()
        scoreboard.l_point()


    if ball.xcor()<-390:
        ball.reset()
        ball.bounce_x()
        scoreboard.r_point()


exit()
screen.exitonclick()