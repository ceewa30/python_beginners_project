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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(WORK_MIN * 60)  # Convert minutes to seconds
    # Here you can add logic to switch between work and break times
    # For example, after WORK_MIN, you can call count_down(SHORT_BREAK_MIN * 60) for a short break
# ---------------------------- RESET TIMER ------------------------------- #

def reset_timer():
    # Reset the timer to initial state
    canvas.itemconfig(timer_text, text="00:00")
    # Reset any other UI elements or variables as needed
    # For example, you can reset the checkmark label or any counters
    checkmark_label.config(text="")

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
        # Here you can add logic to switch to the next timer phase (work/break)
        # For example, you can call start_timer() for the next phase
        window.after(1000, count_down, count - 1)

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
checkmark_label = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset_timer, background=YELLOW, highlightthickness=0, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)









window.mainloop()