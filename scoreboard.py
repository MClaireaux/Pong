from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()

        self.score_l = 0
        self.score_r = 0
        self.turn = 1

        self.goto(position)
        self.color("white")
        self.update()
        self.ht()

    def update(self):
        self.write(arg=f"{self.score_l}     |     {self.score_r}", align=ALIGNMENT, font=FONT)

    def increase_l(self):
        self.score_l += 1
        self.clear()
        self.update()
        self.turn += 1

    def increase_r(self):
        self.score_r += 1
        self.clear()
        self.update()
        self.turn += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
