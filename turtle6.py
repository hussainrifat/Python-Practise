import turtle
turtle.speed(1)

counter=0
while counter<36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
        turtle.right(10)
        counter=counter+1
turtle.exitonclick()