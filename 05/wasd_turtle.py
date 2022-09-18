import turtle
import random

def left_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def up_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
def right_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def down_move():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()
    
def restart():
    turtle.reset()
    turtle.stamp()
    
turtle.shape('turtle')
turtle.stamp()

turtle.onkey(left_move,'a')
turtle.onkey(up_move,'w')
turtle.onkey(right_move,'d')
turtle.onkey(down_move,'s')
turtle.onkey(restart,'Escape')
#turtle.listen()

turtle.exitonclick()