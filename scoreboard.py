from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.color("white")

    def left_score(self, L):
        self.clear()
        self.goto(-50, 300)
        self.write(L, font=("Arial", 42, "normal"))

    def right_score(self, R):
        self.clear()
        self.goto(50, 300)
        self.write(R, font=("Arial", 42, "normal"))




