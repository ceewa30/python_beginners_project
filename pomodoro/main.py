from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)  # Cancel the current timer if it exists
    # Reset the timer to initial state
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps = 0  # Reset the repetition count
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # Start the timer by calling count_down with the initial work time

    # Here you can add logic to switch between work and break times
    # For example, after WORK_MIN, you can call count_down(SHORT_BREAK_MIN * 60) for a short break
    if reps % 8 == 0:
        # Long break
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        # Short break
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        # Work session
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    time_left = f"{minutes}:{seconds}"
    # Update the timer text on the canvas
    canvas.itemconfig(timer_text, text=time_left)
    if count > 0:
        global timer
        # Here you can add logic to switch to the next timer phase (work/break)
        # For example, you can call start_timer() for the next phase
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()  # Automatically start the next timer phase
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create a label for the title
title_label = Label(text="Pomodoro Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create a button for the timer
start_button = Button(window, text="Start", command=start_timer, background=YELLOW, highlightthickness=0, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)


# Create a checkmark label
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset_timer, background=YELLOW, highlightthickness=0, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)



window.mainloop()