import turtle
import pandas

screen = turtle.Screen()    # create a screen
screen.title("U.S. States Game")    # add title to the screen
image = "blank_states_img.gif"   # specify image
screen.addshape(image)  # add image as a new shape

turtle.shape(image)  # set turtle shape to the image

data = pandas.read_csv("50_states.csv")  # read the csv file
all_states = data["state"].to_list()  # get the data series of state column and convert to list alternative: data.state
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    # title() method capitalizes the first letter of the string
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    # check if answer_state is one of the states in all the states in the csv file
    if answer_state in all_states:  # checking for membership using "in" keyword requires list
        # if they got it right:
        # create a turtle to write the name of the state at the state's x and y coordinates
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()  # hide the turtle shape
        t.penup()   # don't draw anything
        state_data = data[data.state == answer_state]   # get a specific row of data
        t.goto(int(state_data.x), int(state_data.y))  # tap into the attributes of row using row.column_name
        t.write(answer_state)
        # t.write(state_data.state.item())   # write the name of the state from the csv file
        # item() method returns the first element of the underlying data


# def get_mouse_click_cor(x, y):
#     """Function that takes two values as input and prints them out"""
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)  # event listener which listen for a mouse click and
# # pass x, y value of the clicked location
#
# turtle.mainloop()   # alternative way of keeping our screen open even though our code has finished running
