import turtle as t
from turtle import Screen
import random

# TODO : Extract Colors From an Image
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     # rgb = (color.rgb[0],color.rgb[1],color.rgb[2])
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
color_list = [(1, 10, 30), (229, 235, 242), (239, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7)]
tim.speed("fastest")

y_position = 0
# TODO : Draw a dotted line 10 x 10
# for _ in range(10): # y axis
#     for _ in range(10): # x axis
#         random_color = random.choice(color_list)
#         tim.pencolor(random_color)
#         tim.penup()
#         tim.dot(20)
#         tim.forward(20)
#         tim.penup()
#         tim.forward(20)
#     y_position += 40
#     tim.teleport(0, y_position)

tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1): # y axis
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()