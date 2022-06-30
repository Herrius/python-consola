
import turtle
from numpy import true_divide
import pandas as pd
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess=0
continue_game=False
state=pd.read_csv("50_states.csv")
all_states=state.state.to_list()
guessed_state=[]
while not continue_game:
    answer_state=screen.textinput(title=f"Guess the state{50-len(all_states)}/50",prompt="What's another state's name?").title()
    print(answer_state)
    answer=state[state.state==answer_state]
    if not answer_state in all_states:
        pass
    else:
        all_states.remove(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(answer['x'].values[0],answer['y'].values[0])
        t.write(f"{answer['state'].values[0]}")