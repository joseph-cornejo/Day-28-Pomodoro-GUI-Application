from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", font=("Arial", 42), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(font=("Arial", 24, "bold"), fg=GREEN, bg=YELLOW)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    #calculates seconds and minutes from count
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    #this is so that its not just 0, or 2 but instead shows 00 or 02. For Example 5:02
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    #puts initial time on counter
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    #timer function, also checks to see if this completes one cucle, if it does it adds a check mark
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        temp_reps = math.floor(reps / 2)
        for check in range(temp_reps):
            mark += "✔"
        check_label.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
#creates window with title
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

#creates canvas, loads image and sets up grid.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)


#labels
timer_label = Label(text="Timer", font=("Arial", 42), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=1)

check_label = Label(font=("Arial", 24, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=4)

#buttons
button1 = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
button1.grid(column=0, row=3)

button2 = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
button2.grid(column=2, row=3)

window.mainloop()