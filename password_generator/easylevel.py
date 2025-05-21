# This code generates a random password based on user input for the number of letters, symbols, and numbers.
# It uses the random and string modules to create a password that includes uppercase and lowercase letters, digits, and punctuation symbols.
# The password is shuffled to ensure randomness and is printed to the user.
# The user is prompted to enter the desired number of letters, symbols, and numbers for the password.
# The password is then generated and displayed to the user.
# The code uses a list to store the characters and then shuffles them to create a random password.
# The password is then printed to the user.

import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to the Easy Level Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for _ in range(nr_letters):
    password_list.append(random.choice(letters))
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")
