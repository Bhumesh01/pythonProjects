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
'''
CANVAS WIDGET:
allows you to lay the things one on to the other,

NOTE:  ALL GUIs ARE EVENT DRIVEN ie THEY KEEP AN EYE ON ALL THE EVENTS THAT ARE TAKING PLACE
THE REFRESH THE SCREEN EVERY MOMENT FOR A SPECIFIC ACTION OR AN EVENT.
HERE IT IS BECAUSE OF mainloop() method that loops through and checks every milli second if something happens.
thus if we have another loop in our program it won't be able to reach the mainloop and nothing happens

Imagine you're at a party, and there's a group of people chatting and having fun. Each person at the party represents 
an event, like someone saying something or doing something.
Now, think of Tkinter as the host of this party. The host's job is to make sure everyone gets to have a good time and 
that everything runs smoothly.
In Tkinter, when you create a window and add buttons, text fields, or other elements, it's like setting up different 
activities at the party. The buttons are like games people can play, and the text fields are places where they can 
write things.
Now, the important part: the event loop. This is like the host keeping an eye on everything happening at the party. 
When someone wants to play a game (like clicking a button), the host needs to be ready to respond and make sure the 
game runs smoothly.
If the host gets distracted or busy doing something else (like being stuck in a while loop), they won't be able to 
pay attention to what's happening at the party. As a result, people might get frustrated because they can't play the 
games or interact with each other.
In Tkinter, using a while loop without considering the event loop is like the host getting distracted. The program 
gets stuck in the loop and doesn't pay attention to what the users are doing (like clicking buttons or typing).
So, to keep the party (your Tkinter application) running smoothly, you should let the event loop do its job. Instead 
of using a while loop, you set up event handlers for different actions (like clicking a button), and Tkinter takes 
care of managing these events while keeping the application responsive and interactive.

however, after() method can be used. it takes the amount of time it should take as an input and the function you tell it 
to call
'''


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
