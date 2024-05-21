from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.hideturtle()
        self.color("white")
        self.update_board()

    def update_board(self):
        self.write(f"score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
