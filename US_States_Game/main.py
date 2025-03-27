import turtle

from pandas.core.interchange.dataframe_protocol import DataFrame

from states import States
import pandas

screen = turtle.Screen()

screen.title("Mahmoud's States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


list_of_guessed_states = []

forgotten = []


while len(list_of_guessed_states) < 50:


    answer = screen.textinput(title=f"{len(list_of_guessed_states)}/50 states correct", prompt="Name another state").title()

    list_of_states = data.state.to_list()

    if answer in list_of_states:
        states_data = data[data.state == answer]

        maps = States(state_name=answer, x_cor=states_data.x.item(), y_cor=states_data.y.item())

        maps.write_name_of_state()

        if answer not in list_of_guessed_states:
            list_of_guessed_states.append(answer)

        if list_of_guessed_states == 50:
            break

    if answer == "Exit":
        for i in list_of_states:
            if i not in list_of_guessed_states:
                forgotten.append(i)
        new_data = pandas.DataFrame(forgotten)
        new_data.to_csv("states_to_learn.csv")
        break

































turtle.mainloop()

