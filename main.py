import turtle

screen = turtle.Screen()    # create a screen
screen.title("U.S. States Game")    # add title to the screen
image = "blank_states_img.gif"   # specify image
screen.addshape(image)  # add image as a new shape

turtle.shape(image)  # set turtle shape to the image

answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?")
print(answer_state)

# def get_mouse_click_coor(x, y):
#     """Function that takes two values as input and prints them out"""
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)  # event listener which listen for a mouse click and
# # pass x, y value of the clicked location
#
# turtle.mainloop()   # alternative way of keeping our screen open even though our code has finished running

