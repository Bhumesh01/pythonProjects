from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score : {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()



    # def game_over(self):
    #     self.clear()
    #     self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over", align="center", font=("Arial", 24, "normal"))
