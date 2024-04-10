from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [130, 80, 30, -20, -70, -120]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_axis[i])
    all_turtles.append(new_turtle)

    new_turtle.position()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                #The location of the text is off the screen for the turtle.write
                #turtle.write(f"You've won! The {winning_color} turtle is the winner!", font=("Arial", 12, "normal"))
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                #turtle.write(f"You've lost! The {winning_color} turtle is the winner!", font=("Arial", 12, "normal"))
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





screen.exitonclick()