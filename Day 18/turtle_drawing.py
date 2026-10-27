from turtle import Turtle, Screen # best if using object a lot
import random
# import turtle # best if calling the object rarely
# from turtle import * # says to import everything, but not the best to use bc it unclear what you're calling
# import turtle as t # assigning an alias

tim = Turtle()
tim.shape("turtle")
tim.color("violet")

# TODO 1: Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# TODO 2: Draw a dashed line
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]
# TODO 3: Draw many shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.pendown()
        tim.forward(50)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()