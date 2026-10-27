import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() # get all states in states column
guessed_states = []

# def check_answer(answer_state):
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's another state's name?").title()

    # save non guessed states to csv
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states] # cut down code using list comprehension
        data = pandas.DataFrame(missing_states) # create new data frame
        data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states: #if answer is right, state gets added with text
        guessed_states.append(answer_state)
        state = data[data.state == answer_state] # gets row with state in it
        x_coord = int(state.x.item()) # in the same row, retrieves specific column
        y_coord = int(state.y.item())

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coord, y_coord)
        t.write(answer_state, align="center", font=("Arial", 15, "normal"))

# game_is_on = True
#
# while game_is_on:
#     answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
#     check_answer(answer_state)
#     print(answer_state)
