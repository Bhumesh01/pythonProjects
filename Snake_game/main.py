import turtle as t
import time
from snake import Snake
from food import Food
from score import Score

screen = t.Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(height=600, width=600)

screen.title("My Snake Game")

snake = Snake()
food = Food()
score_1 = Score()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_1.increase_score()
        score_1.update_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        snake.reset()
        score_1.reset()
        score_1.update_score()
    # detect collision with tail
    for segment in snake.segments[1:]:
        #     if segment != snake.head:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score_1.reset()


    #         else:
    #             pass

screen.exitonclick()
