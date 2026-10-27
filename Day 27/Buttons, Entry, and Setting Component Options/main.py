from tkinter import *

window = Tk() # create a window
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100, pady=200) # add space around item

# TODO: Creating labels
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text" OR
# my_label.config(text="New Text")
my_label.config(padx=50, pady=50)

# TODO: Tkinter Layout Managers - define how to place widgets on grid. This MUST be specified for item to show up on screen
#  pack, place or grid
#  WARNING - you cant mix up grid and pack in the same program
# my_label.pack(side="left") # Use the packer to pack label onto screen/ display it
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

#  TODO: Creating Buttons
def button_clicked():
    print("I got clicked")
    #my_label["text"] = input.get()
    new_text = input.get()
    my_label.config(text=new_text)
button1 = Button(text="Click Me", command=button_clicked) # set event listener if button clicked
button2 = Button(text="ClickMe", command=button_clicked)
button1.grid(column=1, row=1)
button2.grid(column=2, row=0)

# button.pack()

# TODO: Creating Entries - a text box
input = Entry(width=10)
input.grid(column=3, row=3)
# input.pack()



window.mainloop() # keep window on screen. also listens for user interaction
