from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 200)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.write(f"{self.l_score}    {self.r_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_l_score(self):
        self.clear()
        self.l_score += 1
        self.write(f"{self.l_score}    {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_r_score(self):
        self.clear()
        self.r_score += 1
        self.write(f"{self.l_score}    {self.r_score}", align=ALIGNMENT, font=FONT)