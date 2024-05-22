from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.curr_level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.curr_level += 1
        self.clear()
        self.write(f"Level: {self.curr_level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=("Courier", 40, "normal"))
