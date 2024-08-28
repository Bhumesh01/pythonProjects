import time
from score import Score
from turtle import Turtle, Screen
from player import Player
from car_manager import Car
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gold")
screen.tracer(0)
player = Player()
car = Car()
score = Score()
screen.listen()
screen.onkey(fun=player.up, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for i in car.all_cars:
        if i.distance(player) < 25:
            score.game_over()
            game_is_on = False
    if player.is_at_finish_line():
        score.update_score()
        player.go_to_start()
        car.level_up()








screen.exitonclick()