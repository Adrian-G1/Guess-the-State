import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt='Name of a State:').title()

# States to learn
    if answer_state == "Exit":
        with open("states_to_learn.csv", mode='w') as file:
            for state in all_states:
                if state not in guessed_states:
                    file.write(f"{state}\n")
        break

# Check if answer_state in State column
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state = State()
        state.move_state(int(state_data.x), int(state_data.y))
        state.write_state(answer_state)

