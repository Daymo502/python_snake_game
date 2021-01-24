from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.showScore()

    def showScore(self):
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align="center", font=("Arial", 16, "normal"))

    def increment(self):
        self.score += 1
        self.clear()
        self.showScore()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=("Arial", 16, "normal"))
