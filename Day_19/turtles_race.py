import turtle
from turtle import Screen
import random

COLORS = ["green", "yellow", "purple", "red", "blue", "orange"]

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Choose your bet:", prompt="Which turtle will win the race? [green, yellow, purple, red, blue, orange]")
turtles = []
is_race_on = True


# Create all turtles and set their position to the race start line
gap = 0
for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(COLORS[i])
    new_turtle.goto(x=-230, y=-100 + gap)
    gap += 30
    turtles.append(new_turtle)

# Start the race
while is_race_on:
    for racing_turtle in turtles:
        racing_turtle.forward(random.randint(0, 10))

        if racing_turtle.xcor() > 230:
            is_race_on = False
            winning_color = racing_turtle.pencolor()
            if user_bet == winning_color:
                print(f"You win! the {winning_color} turtle has won the race.")
            else:
                print(f"You lost! the {winning_color} turtle has won the race.")

screen.exitonclick()
