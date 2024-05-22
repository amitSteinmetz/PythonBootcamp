from turtle import Turtle

FONT = ("Courier", 60, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_board()

    def update_board(self):
        self.goto(-100, 220)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 220)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_board()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_board()
