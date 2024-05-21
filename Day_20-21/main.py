from turtle import Screen
import time
from food import Food
from snake import Snake
from score_board import ScoreBoard

# Settings #
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

# Control movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Starting the game #

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.07)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score_board.game_over()

    # Detect collision with tail
    if len(snake.segments) > 3:
        for segment in snake.segments[3:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                score_board.game_over()

screen.exitonclick()
