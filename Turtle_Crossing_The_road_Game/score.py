from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.reset()

    def reset(self):
        self.goto(-280, 260)
        self.color("black")
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.reset()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)
