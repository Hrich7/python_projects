"""import colorgram 

colors = colorgram.extract('Hirst_Painting/image.jpg', 30)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
print(rgb_colors)"""

from turtle import Turtle, Screen, colormode
import random

color_list = [(233, 219, 204), (199, 170, 144), (216, 193, 157), (144, 89, 53), (51, 19, 11), 
                (180, 145, 49), (12, 21, 44), (40, 10, 18), (156, 21, 12), (232, 236, 242), 
              (225, 179, 165), (71, 100, 127), (142, 170, 150), (138, 69, 78), (196, 95, 77), (153, 17, 26), 
              (72, 116, 77), (184, 142, 149), (134, 159, 177), (15, 45, 19), (79, 81, 23), (188, 87, 95), 
              (103, 145, 112), (30, 93, 32), (222, 173, 179), (178, 203, 171), (37, 58, 98), (110, 119, 153)]

tim = Turtle()
tim.speed('fastest')
tim.up()
tim.hideturtle()  

screen = Screen()
# Setting the screen color-mode
screen.colormode(255)
print(screen.window_width(), screen.window_height())
#screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

tim.setheading(210)
tim.forward(330)
tim.setheading(0)

for i in range(1, 101):
    color = random.choice(color_list)
    tim.dot(25, color)
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if i % 10 == 0:
        tim.up()
        tim.setheading(90)
        tim.forward(50)
        tim.seth(180)
        tim.forward(500)
        tim.seth(0)
        tim.down

   


"""
tim.fillcolor(color)
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
"""
screen.exitonclick()