# This is a simple number guessing game where the user has to guess a number between 1 and 100.
# The game provides feedback on whether the guess is too low or too high.
# The game continues until the user guesses the correct number, at which point it congratulates them and shows the number of attempts taken.
# The game uses the random module to generate a random number between 1 and 100.
# The user is prompted to enter their guess, and the program checks if the guess is correct.
# The game is played in a loop until the correct number is guessed.
# The user is informed if their guess is too low or too high.
# The game keeps track of the number of attempts made by the user.
# The game ends when the user guesses the correct number, and the total number of attempts is displayed.

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 5
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts -= 1
        if attempts < 0:
            print("Sorry, you've run out of attempts. Better luck next time!")
            break
        print(f"You have {attempts} attempts left.")
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

number_guessing_game()
