from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# TODO: JSON quick reference guide
# write = json.dump()
# read = json.load()
# update = json.update()
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="No Data File Found.")  # if key not found
        return
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")# if key not found

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #  new_list = [new_item for item in list]

    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_numbers = [choice(numbers) for item in range(randint(2, 4))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    # for char in password_list:
    #     password += char
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you haven't left any required fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # read old data / turn data into python dictionary

        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                # File doesn't exist → create it with new_data
                json.dump(new_data, data_file, indent=4)

        else:
            # File exists → update existing data
            data.update(new_data) # update old, dictionaru with new data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
# Tkinter is designed to size the window based on widgets. Let it do that unless you have a specific reason.
# in other words always modify size of widgets, not the window

# display image
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) # Place the image 100 pixels right and 100 pixels down from the top-left corner of the canvas.
canvas.grid(column=1,row=0)

# labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# entry boxes
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus() # put the cursor within the first textbox

email_entry = Entry(width=21)
email_entry.grid(column=1, row=2, columnspan=1)
email_entry.insert(0, "bob@gmail.com") # insert this piece of text at the first character

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

# buttons

generate_password_button = Button(text="Generate Password", command=generate_password) # set event listener if button clicked
generate_password_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", command=save_info, width=36)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, width=13) # set event listener if button clicked
search_button.grid(column=2, row=1)

window.mainloop()