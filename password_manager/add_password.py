# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if not website or not email or not password:
        print("Please fill in all fields.")
        return

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")

    website_text.delete(0, END)
    email_text.delete(0, END)
    password_text.delete(0, END)

    print("Password saved successfully!")