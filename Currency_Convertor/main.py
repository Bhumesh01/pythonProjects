import time
import requests
import pygame
from tkinter import *
from tkinter import messagebox

pygame.mixer.init()

# REQUEST MODULE INFORMATION

API_KEY = "fca_live_8fsa5ChzjUxtbUNeaQ1GbcZuiE2Du3d26ULCEXaF"
body = {
    "apikey": API_KEY
}
response = requests.get(url="https://api.freecurrencyapi.com/v1/currencies", params=body)
print(response.status_code)
currency_data = response.json()
# currency_data = {'data': {'EUR': {'symbol': '€', 'name': 'Euro', 'symbol_native': '€', 'decimal_digits': 2, 'rounding': 0, 'code': 'EUR', 'name_plural': 'Euros', 'type': 'fiat'}, 'USD': {'symbol': '$', 'name': 'US Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'USD', 'name_plural': 'US dollars', 'type': 'fiat'}, 'JPY': {'symbol': '¥', 'name': 'Japanese Yen', 'symbol_native': '￥', 'decimal_digits': 0, 'rounding': 0, 'code': 'JPY', 'name_plural': 'Japanese yen', 'type': 'fiat'}, 'BGN': {'symbol': 'BGN', 'name': 'Bulgarian Lev', 'symbol_native': 'лв.', 'decimal_digits': 2, 'rounding': 0, 'code': 'BGN', 'name_plural': 'Bulgarian leva', 'type': 'fiat'}, 'CZK': {'symbol': 'Kč', 'name': 'Czech Republic Koruna', 'symbol_native': 'Kč', 'decimal_digits': 2, 'rounding': 0, 'code': 'CZK', 'name_plural': 'Czech Republic korunas', 'type': 'fiat'}, 'DKK': {'symbol': 'Dkr', 'name': 'Danish Krone', 'symbol_native': 'kr', 'decimal_digits': 2, 'rounding': 0, 'code': 'DKK', 'name_plural': 'Danish kroner', 'type': 'fiat'}, 'GBP': {'symbol': '£', 'name': 'British Pound Sterling', 'symbol_native': '£', 'decimal_digits': 2, 'rounding': 0, 'code': 'GBP', 'name_plural': 'British pounds sterling', 'type': 'fiat'}, 'HUF': {'symbol': 'Ft', 'name': 'Hungarian Forint', 'symbol_native': 'Ft', 'decimal_digits': 0, 'rounding': 0, 'code': 'HUF', 'name_plural': 'Hungarian forints', 'type': 'fiat'}, 'PLN': {'symbol': 'zł', 'name': 'Polish Zloty', 'symbol_native': 'zł', 'decimal_digits': 2, 'rounding': 0, 'code': 'PLN', 'name_plural': 'Polish zlotys', 'type': 'fiat'}, 'RON': {'symbol': 'RON', 'name': 'Romanian Leu', 'symbol_native': 'RON', 'decimal_digits': 2, 'rounding': 0, 'code': 'RON', 'name_plural': 'Romanian lei', 'type': 'fiat'}, 'SEK': {'symbol': 'Skr', 'name': 'Swedish Krona', 'symbol_native': 'kr', 'decimal_digits': 2, 'rounding': 0, 'code': 'SEK', 'name_plural': 'Swedish kronor', 'type': 'fiat'}, 'CHF': {'symbol': 'CHF', 'name': 'Swiss Franc', 'symbol_native': 'CHF', 'decimal_digits': 2, 'rounding': 0, 'code': 'CHF', 'name_plural': 'Swiss francs', 'type': 'fiat'}, 'ISK': {'symbol': 'Ikr', 'name': 'Icelandic Króna', 'symbol_native': 'kr', 'decimal_digits': 0, 'rounding': 0, 'code': 'ISK', 'name_plural': 'Icelandic krónur', 'type': 'fiat'}, 'NOK': {'symbol': 'Nkr', 'name': 'Norwegian Krone', 'symbol_native': 'kr', 'decimal_digits': 2, 'rounding': 0, 'code': 'NOK', 'name_plural': 'Norwegian kroner', 'type': 'fiat'}, 'HRK': {'symbol': 'kn', 'name': 'Croatian Kuna', 'symbol_native': 'kn', 'decimal_digits': 2, 'rounding': 0, 'code': 'HRK', 'name_plural': 'Croatian kunas', 'type': 'fiat'}, 'RUB': {'symbol': 'RUB', 'name': 'Russian Ruble', 'symbol_native': 'руб.', 'decimal_digits': 2, 'rounding': 0, 'code': 'RUB', 'name_plural': 'Russian rubles', 'type': 'fiat'}, 'TRY': {'symbol': 'TL', 'name': 'Turkish Lira', 'symbol_native': 'TL', 'decimal_digits': 2, 'rounding': 0, 'code': 'TRY', 'name_plural': 'Turkish Lira', 'type': 'fiat'}, 'AUD': {'symbol': 'AU$', 'name': 'Australian Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'AUD', 'name_plural': 'Australian dollars', 'type': 'fiat'}, 'BRL': {'symbol': 'R$', 'name': 'Brazilian Real', 'symbol_native': 'R$', 'decimal_digits': 2, 'rounding': 0, 'code': 'BRL', 'name_plural': 'Brazilian reals', 'type': 'fiat'}, 'CAD': {'symbol': 'CA$', 'name': 'Canadian Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'CAD', 'name_plural': 'Canadian dollars', 'type': 'fiat'}, 'CNY': {'symbol': 'CN¥', 'name': 'Chinese Yuan', 'symbol_native': 'CN¥', 'decimal_digits': 2, 'rounding': 0, 'code': 'CNY', 'name_plural': 'Chinese yuan', 'type': 'fiat'}, 'HKD': {'symbol': 'HK$', 'name': 'Hong Kong Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'HKD', 'name_plural': 'Hong Kong dollars', 'type': 'fiat'}, 'IDR': {'symbol': 'Rp', 'name': 'Indonesian Rupiah', 'symbol_native': 'Rp', 'decimal_digits': 0, 'rounding': 0, 'code': 'IDR', 'name_plural': 'Indonesian rupiahs', 'type': 'fiat'}, 'ILS': {'symbol': '₪', 'name': 'Israeli New Sheqel', 'symbol_native': '₪', 'decimal_digits': 2, 'rounding': 0, 'code': 'ILS', 'name_plural': 'Israeli new sheqels', 'type': 'fiat'}, 'INR': {'symbol': 'Rs', 'name': 'Indian Rupee', 'symbol_native': 'টকা', 'decimal_digits': 2, 'rounding': 0, 'code': 'INR', 'name_plural': 'Indian rupees', 'type': 'fiat'}, 'KRW': {'symbol': '₩', 'name': 'South Korean Won', 'symbol_native': '₩', 'decimal_digits': 0, 'rounding': 0, 'code': 'KRW', 'name_plural': 'South Korean won', 'type': 'fiat'}, 'MXN': {'symbol': 'MX$', 'name': 'Mexican Peso', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'MXN', 'name_plural': 'Mexican pesos', 'type': 'fiat'}, 'MYR': {'symbol': 'RM', 'name': 'Malaysian Ringgit', 'symbol_native': 'RM', 'decimal_digits': 2, 'rounding': 0, 'code': 'MYR', 'name_plural': 'Malaysian ringgits', 'type': 'fiat'}, 'NZD': {'symbol': 'NZ$', 'name': 'New Zealand Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'NZD', 'name_plural': 'New Zealand dollars', 'type': 'fiat'}, 'PHP': {'symbol': '₱', 'name': 'Philippine Peso', 'symbol_native': '₱', 'decimal_digits': 2, 'rounding': 0, 'code': 'PHP', 'name_plural': 'Philippine pesos', 'type': 'fiat'}, 'SGD': {'symbol': 'S$', 'name': 'Singapore Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'SGD', 'name_plural': 'Singapore dollars', 'type': 'fiat'}, 'THB': {'symbol': '฿', 'name': 'Thai Baht', 'symbol_native': '฿', 'decimal_digits': 2, 'rounding': 0, 'code': 'THB', 'name_plural': 'Thai baht', 'type': 'fiat'}, 'ZAR': {'symbol': 'R', 'name': 'South African Rand', 'symbol_native': 'R', 'decimal_digits': 2, 'rounding': 0, 'code': 'ZAR', 'name_plural': 'South African rand', 'type': 'fiat'}}}
codes_list = [keys for keys in currency_data["data"]]
result = requests.get(url="https://api.freecurrencyapi.com/v1/latest", params=body)
print(result.status_code)
exchange_rates = result.json()
# exchange_rates = {'data': {'AUD': 1.4829601975, 'BGN': 1.8042602886, 'BRL': 5.4712505661, 'CAD': 1.3630901473, 'CHF': 0.8976901143, 'CNY': 7.2658408338, 'CZK': 23.2226944038, 'DKK': 6.8856911945, 'EUR': 0.9230701175, 'GBP': 0.7803100938, 'HKD': 7.8086510947, 'HRK': 6.6057210677, 'HUF': 364.2641334805, 'IDR': 16230.240623863, 'ILS': 3.6857203781, 'INR': 83.430099795, 'ISK': 137.7647432695, 'JPY': 160.833089708, 'KRW': 1380.6828492129, 'MXN': 17.9786828428, 'MYR': 4.7074106665, 'NOK': 10.6017811417, 'NZD': 1.6311202882, 'PHP': 58.5249105487, 'PLN': 3.9388806052, 'RON': 4.5921208561, 'RUB': 87.5688772975, 'SEK': 10.5817212172, 'SGD': 1.3493902696, 'THB': 36.3997238876, 'TRY': 32.6937152039, 'USD': 1, 'ZAR': 18.0969018472}}
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
