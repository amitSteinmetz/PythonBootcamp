import turtle
from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/{len(all_states)} states correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    # Check if the guess is among the 50 states
    if answer_state in all_states:
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_data = data[data.state == answer_state]
        x_coor = state_data.x.values[0]
        y_coor = state_data.y.values[0]
        state_turtle.goto(x_coor, y_coor)
        state_turtle.write(answer_state)
        correct_answers.append(answer_state)

screen.exitonclick()

# Save missing states to csv file
missing_states = []
for state in all_states:
    if state not in correct_answers:
        missing_states.append(state)

missing_states_df = pandas.DataFrame(missing_states)
missing_states_df.to_csv("learn_states.csv")

