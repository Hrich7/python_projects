from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.setheading(180)
    tim.forward(10)
    #or tim.backward(10)

def counter_clockwise():
    tim.left(15)

def clockwise():
    tim.right(15)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown() 

"""
    W = forward
    S = Backward
    A = counter - clockwise
    D + clockwise
    C = Clear drawing
"""

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()