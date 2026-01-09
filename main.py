from turtle import Screen
from paddle import Paddle
from border import border

screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.canvheight = 600
screen.canvwidth = 800
screen.tracer(0)

border = border

paddle_left = Paddle(440,0)
paddle_right = Paddle(-440,0)

# move up and down,
up_l = screen.onkeypress(paddle_left.move_up, "Up")
down_l = screen.onkeypress(paddle_left.move_down, "Down")

up_r = screen.onkeypress(paddle_right.move_up, "w")
down_r = screen.onkeypress(paddle_right.move_down, "s")




game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
