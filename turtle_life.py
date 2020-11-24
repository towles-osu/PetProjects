# Author:stew
# Date:time
# Description: playing with turtle

import turtle

window = turtle.Screen()
turty = turtle.Turtle()

def draw_pen15(a_turtle):
    a_turtle.forward(80)
    a_turtle.right(80)
    a_turtle.forward(12)
    a_turtle.left(90)
    a_turtle.forward(9)
    a_turtle.left(15)
    a_turtle.forward(10)
    a_turtle.left(30)
    a_turtle.forward(10)
    a_turtle.left(25)
    a_turtle.forward(10)
    a_turtle.left(25)
    a_turtle.forward(10)
    a_turtle.left(30)
    a_turtle.forward(10)
    a_turtle.left(15)
    a_turtle.forward(9)
    a_turtle.left(90)
    a_turtle.forward(12)
    a_turtle.right(80)
    a_turtle.forward(80)

turty.forward(120)
print(turty.pos())
turty.left(90)
print(turty.pos())
window.bgcolor('purple')
draw_pen15(turty)




window.exitonclick()