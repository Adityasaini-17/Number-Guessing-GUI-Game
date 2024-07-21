from tkinter import *
import random

# Function to user's guess
def check_guess():
    try:
        user_guess = int(guess_entry.get())
        global attempts
        attempts += 1
        if user_guess < number:
            result.set("Too low! Try again.")
        elif user_guess > number:
            result.set("Too high! Try again.")
        else:
            result.set(f"Correct! You guessed the number in {attempts} attempts.")
    except ValueError:
        result.set("Please enter a valid number.")

# Function reset the game
def reset_game():
   
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, END)
    result.set("")

# main window
root = Tk()
root.title("Guessing Game")
root.geometry("400x300")
root.resizable(False, False)

# Variables
number = random.randint(1, 100)
attempts = 0
result = StringVar()

# user's guess
guess_label = Label(root, text="Enter your guess (1-100):", font="lucida 12")
guess_label.pack(pady=10)

guess_entry = Entry(root, font="lucida 14")
guess_entry.pack(pady=5)

# check guess
check_button = Button(root, text="Check Guess", command=check_guess, font="lucida 12")
check_button.pack(pady=10)

# display result
result_label = Label(root, textvariable=result, font="lucida 8 bold")
result_label.pack(pady=10)
 
# reset the game
reset_button = Button(root, text="Reset Game", command=reset_game, font="lucida 12")
reset_button.pack(pady=10)

# main loop
root.mainloop()
