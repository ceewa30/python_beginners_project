# Hello world GUI application

from tkinter import Tk, Label, Button, StringVar, Entry

def on_button_click():
    user_input = input_var.get()
    print("User input:", user_input)
    label2.config(text=f"You entered: {user_input}")

app = Tk()
app.title("Hello World GUI")
app.minsize(width=500, height=500)

app.config(padx=20, pady=20)

input_var = StringVar()
input_label = Label(app, text="Enter something:")
input_label.pack()

label2 = Label(app, text="")
label2.pack()


input_entry = Entry(app, textvariable=input_var)
input_entry.pack()

submit_button = Button(app, text="Submit", command=on_button_click)
submit_button.pack()

app.mainloop()