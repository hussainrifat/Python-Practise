import turtle
a=turtle.Turtle()
a.speed(1)
for i in range(4):
    a.forward(100)
    for j in range(4):
        a.forward(100)
        a.left(90)
turtle.exitonclick()
