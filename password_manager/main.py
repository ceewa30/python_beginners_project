from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
# from add_password import add_password


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    nr_letters = random.randint(8, 10)
    nr_digits = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list= []
    password_list.extend(random.sample(letters, nr_letters))
    password_list.extend(random.sample(digits, nr_digits))
    password_list.extend(random.sample(symbols, nr_symbols))

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)  # Copy the generated password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if not website or not email or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        website_text.focus()
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

    website_text.delete(0, END)
    email_text.delete(0, END)
    password_text.delete(0, END)

    messagebox.showinfo("Success", "Password saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white", cursor='cross')


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0, highlightbackground="white", borderwidth=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1, columnspan=3)

website_label = Label(text="Website: ", bg="white", fg="black", font=("Arial", 16, "bold"), padx=10, pady=10)
website_label.grid(column=1, row=2)

website_text = Entry(window,width=40, font=("Arial", 16), highlightthickness=0, fg="black", highlightbackground="white", borderwidth=1, bg="white")
website_text.config(cursor='xterm')
website_text.grid(column=2, row=2, columnspan=2)
website_text.focus()

email_label = Label(text="Email/Username: ", bg="white", fg="black", font=("Arial", 16, "bold"), padx=10, pady=10)
email_label.grid(column=1, row=3)

email_text = Entry(width=40, font=("Arial", 16), highlightthickness=0, fg="black",highlightbackground="white", borderwidth=1, bg="white")
email_text.grid(column=2, row=3, columnspan=2)
# email_text.insert(0, "Add your email here")  # Optional placeholder text

password_label = Label(text="Password: ", bg="white", fg="black", font=("Arial", 16, "bold"), padx=10, pady=10)
password_label.grid(column=1, row=4)

password_text = Entry(width=21, font=("Arial", 16), highlightthickness=0, fg="black", highlightbackground="white", borderwidth=1, bg="white")
password_text.grid(column=2, row=4)

generate_button = Button(text="Generate Password", command=generate_password, width=12, font=("Arial", 16), highlightthickness=0, fg="black", highlightbackground="white", borderwidth=1, bg="white", padx=10)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=36, font=("Arial", 16), highlightthickness=0, fg="black", highlightbackground="white", borderwidth=1, bg="white", padx=10, command=add_password)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()