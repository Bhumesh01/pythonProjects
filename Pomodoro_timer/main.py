# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math

PINK = "#e2979c"  # HexCode
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_details = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer_details)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Work", fg=GREEN)
    checkmark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds <= 9:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer_details
        timer_details = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        for i in range(0, math.floor(reps / 2)):
            marks += "✔"
        checkmark_label.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", width=10, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=10, command=reset_timer)
reset_button.grid(column=2, row=2)
checkmark_label = Label(fg=GREEN, font=(FONT_NAME, 18, "bold"), highlightthickness=0)
checkmark_label.grid(column=1, row=2)

window.mainloop()
