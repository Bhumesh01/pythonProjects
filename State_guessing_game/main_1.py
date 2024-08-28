import turtle
import pandas
background = turtle.Turtle()
screen = turtle.Screen()
image = "India_Map_image.gif"
screen.addshape(image)
background.shape(image)
text = turtle.Turtle()
data = pandas.read_csv("28_indian_states.csv")
state_name = data["state"]
x_cor = data["x"]
y_cor = data["y"]
state_dict = dict(zip(state_name, zip(x_cor, y_cor)))
guessed_states = []
while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 28 States Guessed !", prompt="Enter The State Name ").title()
    if answer_state in state_name.tolist() and answer_state not in guessed_states:
        text.penup()
        text.goto(state_dict[answer_state])
        text.write(answer_state)

        guessed_states.append(answer_state)
    if answer_state == "Exit":
        states_to_learn = [state for state in state_name.tolist() if state not in guessed_states]
        dataframe_states_learn = pandas.DataFrame(states_to_learn)
        dataframe_states_learn.to_csv("states_to_learn_india")
        break

screen.exitonclick()