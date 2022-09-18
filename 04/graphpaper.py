import turtle

y=-1
while(y<500):
    turtle.penup()
    turtle.goto(0,y)
    turtle.pendown()
    turtle.forward(500)
    y+=100
turtle.penup()
turtle.goto(0,-100)
turtle.left(90)
x=1
while(x<=600):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(x,-100)
    x+=100

turtle.exitonclick()