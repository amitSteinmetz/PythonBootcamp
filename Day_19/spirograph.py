import turtle
from turtle import Turtle, Screen
import random

# COLORS_BANK = ["gold", "red", "salmon", "pink", "yellow", "blue", "purple", "gray"]
turtle.colormode(255)
my_turtle = Turtle()
screen = Screen()

my_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(360 // size_of_gap):
        my_turtle.color(random_color())
        my_turtle.setheading(my_turtle.heading() + size_of_gap)
        my_turtle.circle(100)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def move_and_turn_right(turtle_obj, angle):
    turtle_obj.forward(100)
    turtle_obj.right(angle)


def square(turtle_obj):
    for _ in range(4):
        move_and_turn_right(turtle_obj, 90)


def dashed_line(turtle_obj):
    for _ in range(15):
        turtle_obj.forward(10)
        turtle_obj.color("white")
        turtle_obj.forward(10)
        turtle_obj.color("black")


def create_shape(turtle_obj, num_of_edges):
    angle = 360/num_of_edges

    for _ in range(num_of_edges):
        move_and_turn_right(turtle_obj, angle)


def many_shapes(turtle_obj):
    for edges in range(3, 11):
        create_shape(turtle_obj, edges)
        shape_color = random_color()
        turtle_obj.color(shape_color)


# square(my_turtle)
# dashed_line(my_turtle)
# many_shapes(my_turtle)
draw_spirograph(10)


screen.exitonclick()
