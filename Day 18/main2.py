import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]
# TODO 5: Generate random RGB colors
# tuples are a datatype
# you can't change the values in tuples (immutable), unlike lists
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color

# TODO 4: Generate a random walk
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color((random_color()))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# TODO 6: Generate a spirograph
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()