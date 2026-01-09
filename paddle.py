from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__(visible=False)
        self.create_paddle()
        self.Y = 0
        self.paddle.goto(x,y)


    def create_paddle(self):
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.speed(0)
        self.paddle.shapesize(4, 1)

    # def start_position(self, x, y):

    def move_up(self):
        self.Y += 20
        self.paddle.sety(self.Y)

    def move_down(self):
        self.Y -= 20

        self.paddle.sety(self.Y)
