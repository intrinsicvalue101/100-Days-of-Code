import tkinter

window = tkinter.Tk() # create a window
window.title("My First GUI Program")
window.minsize(width=500,height=300)

# label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left") # use the packer to pack label onto screen

# default values passed within function header
import turtle
tim = turtle.Turtle()
tim.write("Some Text") #



window.mainloop() # keep window on screen. also listens for user interaction

