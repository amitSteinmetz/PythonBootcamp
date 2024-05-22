import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.go_up, "Up")

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect reaching to finish line
    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        score_board.update_scoreboard()

screen.exitonclick()
