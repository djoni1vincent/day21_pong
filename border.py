from turtle import Turtle, goto, pendown, penup


border = Turtle(visible=False)

border.speed(0)
border.color("white")
border.penup()
border.goto(460,-225)
border.pendown()


for _ in range(2):
    border.left(90)
    border.fd(450)
    border.left(90)
    border.fd(925)

