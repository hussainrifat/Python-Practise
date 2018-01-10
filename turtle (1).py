import turtle
a=turtle.Turtle()
a.speed(0)
a.color("red")
counter=0
while (counter<=36):
    for i in range(4):
        a.forward(100)
        a.left(90)
    a.right(10)
    counter+=1
counter2=0
while (counter2<= 36):
    for j in range(4):
        a.forward(150)
        a.left(90)
    a.right(10)
    counter2+= 1

turtle.exitonclick()