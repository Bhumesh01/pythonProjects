import smtplib
import random
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv
import pandas
import os

window = Tk()
window.title("Birthday Wisher")
load_dotenv()


def send_birthday_email():
    person_name = name.get()
    birthday_person_name = birthday_name.get()
    birthday_person_mail = birthday_email.get()
    try:
        letters = ["data_1.txt", "data_2.txt", "data_3.txt"]
        random_letter = random.choice(letters)
        with open(file=random_letter, mode="r") as file:
            data = file.read()
        new_data = data.replace("[NAME]", birthday_person_name)
        message = new_data.replace("[SENDER]", person_name)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_person_mail,
                                 msg=f"Subject:Happy Birthday! \n\n {message}")
    except smtplib.SMTPRecipientsRefused:
        messagebox.showerror(title="Oops", message="Check your Gmail id")
    except Exception as e:
        messagebox.showerror(title="Error!", message=f"An error occurred: {str(e)}")
        window.destroy()
    else:
        messagebox.showinfo(title="Yay!",
                            message=f"{person_name}, Your message has been sent to {birthday_person_name}")
        window.destroy()


# UI SET-UP
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
photo = PhotoImage(file="birthday-emails-scaled.png")
canvas = Canvas(width=650, height=577)
canvas_bg = canvas.create_image(325, 288.5, image=photo)
canvas.config(highlightthickness=0)

text_label = Label(window, text="Welcome!🥳", bg="yellow", font=("Comic Sans MS", 30, "bold"))
text_win = canvas.create_window(200, 100, anchor="w", window=text_label)

button_1 = Button(window, text="Next", bg="yellow", width=15, font=("Comic Sans MS", 18, "bold"),
                  command=send_birthday_email)
button_1_win = canvas.create_window(600, 550, anchor="se", window=button_1)

name_label = Label(window, text="Enter your name :", width=29, bg="#87CEEB", font=("Comic Sans MS", 14, "bold"))
name_win = canvas.create_window(10, 250, anchor="w", window=name_label)
name = Entry(window, bg="#87CEEB", font=("Comic Sans MS", 14, "bold"))
name_entry = canvas.create_window(380, 250, anchor="w", window=name)

birthday_name_label = Label(window, text="Enter the birthday person's name:", width=29, bg="#87CEEB",
                            font=("Comic Sans MS", 14, "bold"))
birthday_name_win = canvas.create_window(10, 300, anchor="w", window=birthday_name_label)
birthday_name = Entry(window, bg="#87CEEB", font=("Comic Sans MS", 14, "bold"))
birthday_name_entry = canvas.create_window(380, 300, anchor="w", window=birthday_name)

date_label = Label(window, text="Enter the birth date(YYYY-MM-DD) :", width=29, bg="#87CEEB",
                   font=("Comic Sans MS", 14, "bold"))
date_win = canvas.create_window(10, 350, anchor="w", window=date_label)
birthday_date = Entry(window, bg="#87CEEB", font=("Comic Sans MS", 14, "bold"))
birthday_date_entry = canvas.create_window(380, 350, anchor="w", window=birthday_date)

birthday_email_label = Label(window, text="Enter the birthday person's email id:", width=29, bg="#87CEEB",
                             font=("Comic Sans MS", 14, "bold"))
birthday_email_win = canvas.create_window(10, 400, anchor="w", window=birthday_email_label)
birthday_email = Entry(window, bg="#87CEEB", font=("Comic Sans MS", 14, "bold"))
birthday_email_entry = canvas.create_window(380, 400, anchor="w", window=birthday_email)

canvas.grid(column=0, row=0)


window.mainloop()
