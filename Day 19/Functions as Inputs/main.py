from turtle import Turtle, Screen

# TODO : Passing in a function as input without explictly calling it
# Higher order functions can work with other functions
# Very useful when we have to listen to events and trigger another function
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()