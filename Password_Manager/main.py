from tkinter import *
# this imports all the classes, constants but not the messagebox
from tkinter import messagebox
import random
# pyperclip helps to perform all the functions related to clipboard
import pyperclip
import json

'''
STANDARD DIALOGS: POPUPS
import messagebox module and use methods like showinfo dialog, showwarning dialog, showerror dialog,
askquestion dialog
'''


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_1 = [random.choice(letters) for letter in range(random.randint(8, 10))]
    pass_2 = [random.choice(numbers) for num in range(random.randint(2, 4))]
    pass_3 = [random.choice(symbols) for syb in range(random.randint(2, 4))]
    password_list = pass_1 + pass_2 + pass_3
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_name = website_input.get()
    email_name = email_input.get()
    password_name = password_input.get()
    new_data = {
        website_name: {
            "email": email_name,
            "password": password_name,
        }
    }

    if len(website_name) == 0 or len(password_name) == 0 or len(email_name) == 0:
        messagebox.showerror(title="Oops", message="Please Don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.JSONDecodeError:
            # Handle empty or invalid JSON file
            messagebox.showwarning(title="Warning", message="The data file is empty or corrupt. Creating a new one.")
            data = {}
        else:
            # updating the old data with new data
            data.update(new_data)

        with open("data.json", mode="w") as data_file:
            # saving the updated data
            json.dump(data, data_file, indent=4)

        website_input.delete(0, END)
        email_input.delete(0, END)
        email_input.insert(END, string="bhumeshmahajan01@gmail.com")
        password_input.delete(0, END)
def search_command():
    website_name = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="No Data File Found.")
    else:
        if website_name in data:
            value = data[website_name]
            messagebox.showinfo(title=website_name,
                                message=f"Email : {value['email']} \n Password : {value['password']}")

        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Creating The Entries
website_input = Entry(width=33)
website_input.focus()
website_input.grid(column=1, row=1)
email_input = Entry(width=52)
email_input.insert(index=END, string="bhumeshmahajan01@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Creating The Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Creating The Buttons
generate_password_button = Button(text="Generate Password", command=pass_generator)
generate_password_button.grid(column=2, row=3)
search_button = Button(text="Search", width=15, command=search_command)
search_button.grid(column=2, row=1)
add_button = Button(text="Add", width=44, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
