import turtle

i=-1
while(i<5):
    turtle.penup()
    turtle.goto(0,100*i)
    turtle.pendown()
    turtle.forward(500)
    i+=1
turtle.penup()
turtle.goto(0,-100)
turtle.left(90)
i=1
while(i<=6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(100*i,-100)
    i+=1

turtle.exitonclick()