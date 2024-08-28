import os
import time
import requests
import pygame
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv

pygame.mixer.init()

# REQUEST MODULE INFORMATION
load_dotenv()
api_key = os.getenv("API_KEY")
body = {
    "apikey": api_key
}
response = requests.get(url="https://api.freecurrencyapi.com/v1/currencies", params=body)
currency_data = response.json()
codes_list = [keys for keys in currency_data["data"]]
result = requests.get(url="https://api.freecurrencyapi.com/v1/latest", params=body)
exchange_rates = result.json()
exchange_rates_dict = {key: value for key, value in exchange_rates["data"].items()}

# UI SETUP
window = Tk()
window.title("Currency Convertor")
photo = PhotoImage(file="currency_background.png")
canvas = Canvas(width=626, height=250, highlightthickness=0)
canvas.create_image(313, 125, image=photo)


def conversion():
    base = base_code_clicked.get()
    final = final_code_clicked.get()
    given_amount = value_to_convert.get()
    final_code_rate = exchange_rates_dict[final]
    base_code_rate = exchange_rates_dict[base]
    try:
        if base == "USD":
            converted_amount = float(final_code_rate) * float(given_amount)
            converted_amount_label = Label(text=converted_amount, bg="silver", font=("Arial", 18, "bold"), fg="dark blue")
            converted_amount_label_win = canvas.create_window(300, 200, anchor="w", window=converted_amount_label)
        if base == final:
            label_amount = Label(text=given_amount, bg="silver", font=("Arial", 18, "bold"), fg="dark blue")
            label_amount_win = canvas.create_window(300, 200, anchor="w", window=label_amount)
        else:
            final_amount = (float(given_amount) * float(final_code_rate)) / float(base_code_rate)
            final_amount_label = Label(text=final_amount, bg="silver", font=("Arial", 18, "bold"), fg="dark blue")
            final_amount_label_win = canvas.create_window(300, 200, anchor="w", window=final_amount_label)
    except ValueError:
        messagebox.showerror(title="Oops", message="Check the inputted value.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error {str(e)} has occurred.")
    else:
        time.sleep(1)
        pygame.mixer.music.load("end.mp3")
        pygame.mixer.music.play()


text = Label(text="Currency Convertor", bg="#00005C", font=("Arial", 28, "bold"), fg="#46C2CB")
text_win = canvas.create_window(65, 30, anchor="w", window=text)

amount = Label(text="Amount:", bg="#FFCACC", font=("Arial", 18, "bold"), fg="#C80036")
amount_win = canvas.create_window(20, 150, anchor="w", window=amount)
value_to_convert = Entry(bg="white", font=("Arial", 18, "bold"), fg="#C80036")
value_to_convert_win = canvas.create_window(150, 150, anchor="w", window=value_to_convert)

from_label = Label(text="From:", bg="#F70209", font=("Arial", 18, "bold"), fg="#F5D093")
from_win = canvas.create_window(20, 80, anchor="w", window=from_label)
base_code_clicked = StringVar()
base_code_clicked.set("INR")
base_codes = OptionMenu(window, base_code_clicked, *codes_list)
base_codes.config(bg="yellow")
base_codes_win = canvas.create_window(120, 80, anchor="w", window=base_codes, width=200)

to_label = Label(text="To:", bg="#F70209", font=("Arial", 18, "bold"), fg="#F5D093")
to_win = canvas.create_window(350, 80, anchor="w", window=to_label)
final_code_clicked = StringVar()
final_code_clicked.set("USD")
final_codes = OptionMenu(window, final_code_clicked, *codes_list)
final_codes.config(bg="yellow")
final_codes_win = canvas.create_window(420, 80, anchor="w", window=final_codes, width=200)

button = Button(text="Convert", command=conversion, bg="#FF204E", font=("Arial", 15, "bold"), fg="#FFF5E1")
button_win = canvas.create_window(480, 150, anchor="w", window=button)

answer = Label(text="Converted Amount:", bg="silver", font=("Arial", 18, "bold"), fg="dark blue")
answer_win = canvas.create_window(20, 200, anchor="w", window=answer)

canvas.grid(row=0, column=0)

pygame.mixer.music.load("intro.mp3")
pygame.mixer.music.play()


window.mainloop()
