from turtle import Turtle, Screen
import random


timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

screen = Screen()
screen.bgcolor("black")

#timmy.up()
#timmy.goto(-300,50)
#timmy.down()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)
    #timmy.pencolor(R, G, B)


def draw_shapes():
    for i in range(3, 11):
        change_color()
        angle = 360 / i
        for j in range(i):
            timmy.forward(100)
            timmy.right(angle)

def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


def draw_dashes():
    for _ in range(50):
        timmy.forward(5)
        timmy.up()
        timmy.forward(5)
        timmy.down()

def random_walk():
    timmy.pensize(10)
    change_color()
    #timmy.speed('fastest')
    timmy.left(90) if random.randint(0,1) == 0 else timmy.right(90)
    direction = random.randint(0,1)
    """if direction == 0:
        timmy.left(90)
    else:
        timmy.right(90)"""
    timmy.forward(50)

def random_walk2():
    direction = [0, 90, 180, 270]
    timmy.pensize(10)
    change_color()
    timmy.forward(30)
    timmy.setheading(random.choice(direction))



def draw_spirograph():
    change_color()
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)

def draw_spirograph2(size_of_gap):
    """Stops after a complete rotation with a set gap"""
    timmy.speed('fastest')
    for _ in range(int(360 / size_of_gap)):
        change_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

"""for _ in range(200):
    #random_walk2()
    timmy.speed('fastest')
    draw_spirograph()
"""
draw_spirograph2(5)

screen.exitonclick()