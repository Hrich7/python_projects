import turtle
import pandas as pd

TOTAL_STATES = 50
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")
image = '/home/rico/Documents/Python_scripts/US_States_game/blank_states_img.gif'
# The image moves with the turtle (turtle.goto(x,y)) when using the below methods
# To use screen.addshape and turtle.shape we need to create a turtle instance to use the goto or use screen.bgpic(image)
screen.addshape(image)
turtle.shape(image)
# screen.bgpic(image)


data = pd.read_csv('US_States_game/50_states.csv')
all_states = data["state"].to_list()
guessed_states = []


def update_screen(text, xcor, ycor):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(xcor, ycor)  
    t.write(text, align=ALIGNMENT, font=FONT)


while len(guessed_states) < 50:
    answer_state= turtle.textinput(title=f"{len(guessed_states)}/{TOTAL_STATES} States Correct", 
                                  prompt="What's another state name?").title()
    
    if answer_state == "Exit":
        missed_states = {"missed_states" : [state for state in all_states if state not in guessed_states]}
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("US_States_game/states_to_learn.csv")
        break
    
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        xcor = int(state_data.x.iloc[0])
        ycor = int(state_data.y.iloc[0])
        update_screen(answer_state, xcor, ycor)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)


def get_mouse_click_coor(x, y):
    print(x, y)
#print(turtle.onscreenclick(get_mouse_click_coor))
#screen.exitonclick()

#turtle.mainloop() # -- We breaking out of the loop so this is not needed