from tkinter import *

window = Tk() # create a window
window.title("Mile to Km Converter")

# TODO: Text box
miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

# text = Text(height=5, width=15)
# text.focus() #Puts cursor in textbox.
# text.config(padx=10, pady=10)
# text.grid(column=1,row=0)

# TODO: Creating labels
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

#TODO: Buttons
def miles_to_km():
    miles = float(miles_input.get()) #Get's current value in textbox at line 1, character 0
    kilometers = round(miles * 1.609, 2)
    # TODO: Creating labels
    km_label = Label(text=f"{kilometers}")
    km_label.grid(column=1, row=1)

#calls action() when pressed
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1,row=2)

window.mainloop() # keep window on screen. also listens for user interaction
