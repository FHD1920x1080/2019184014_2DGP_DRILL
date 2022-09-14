import turtle

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.forward(500)
turtle.penup()
i=0
while(i<5):
    turtle.goto(0,100*i)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    i+=1

turtle.goto(0,-100)
turtle.left(90)
i=1
while(i<=6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(100*i,-100)
    turtle.pendown()
    i+=1

turtle.exitonclick()