# from turtle import Turtle, Screen
#
# # creating objects
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan") # changing the color of our object via a method
# timmy.forward(100) # move the turtle forward
#
# my_screen = Screen()
# print(my_screen.canvheight) # printing object attributes, things it has
#
# # calling object methods, things the object can do
# my_screen.exitonclick() # keep running until we click on the screen

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu \nSquirtle \nCharmander"])
table.add_column("Type", ["Electric \nWater \nFire"])

table.align = "l"
print(table)
