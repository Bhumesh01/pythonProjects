from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
#SCREEN
screen = Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Score()
ball = Ball()

screen.listen()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()
        score.l_score_1()

    if ball.xcor() < -380:
        ball.ball_reset()
        score.r_score_1()

    if score.r_score == 5 or score.l_score == 5:
        score.home()
        score.write(arg="GAME OVER", align="center", font=("Courier", 80, "normal"))
        game_is_on = False
screen.exitonclick()
