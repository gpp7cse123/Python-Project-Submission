import tkinter as tk
from tkinter import messagebox
import random


# ---------------- GAME VARIABLES ----------------

number = 0
attempts = 0
max_attempts = 7
score = 100
game_over = False


# ---------------- NEW GAME ----------------

def new_game():
    global number, attempts, max_attempts, score, game_over

    difficulty = difficulty_var.get()

    if difficulty == "Easy":
        number = random.randint(1, 50)
        max_attempts = 10

    elif difficulty == "Medium":
        number = random.randint(1, 100)
        max_attempts = 7

    else:
        number = random.randint(1, 500)
        max_attempts = 6

    attempts = 0
    score = 100
    game_over = False

    guess_entry.delete(0, tk.END)

    message_label.config(
        text="🎯 Guess the number!"
    )

    attempts_label.config(
        text=f"Attempts: 0 / {max_attempts}"
    )

    score_label.config(
        text="Score: 100"
    )

    history_label.config(
        text="Your guesses: "
    )

    guess_button.config(
        state=tk.NORMAL
    )


# ---------------- CHECK GUESS ----------------

def check_guess():

    global attempts, score, game_over

    if game_over:
        message_label.config(
            text="Click New Game to play again."
        )
        return

    try:
        guess = int(guess_entry.get())

    except ValueError:
        message_label.config(
            text="⚠️ Please enter a valid number!"
        )
        return

    difficulty = difficulty_var.get()

    if difficulty == "Easy":
        maximum = 50

    elif difficulty == "Medium":
        maximum = 100

    else:
        maximum = 500

    if guess < 1 or guess > maximum:
        message_label.config(
            text=f"Enter a number between 1 and {maximum}."
        )
        return

    attempts += 1

    # Show guess history
    old_history = history_label.cget("text")

    history_label.config(
        text=old_history + str(guess) + "  "
    )

    attempts_label.config(
        text=f"Attempts: {attempts} / {max_attempts}"
    )

    # Correct answer
    if guess == number:

        bonus = (max_attempts - attempts) * 10
        score += bonus

        message_label.config(
            text="🎉 Congratulations! Correct Number!"
        )

        score_label.config(
            text=f"Score: {score}"
        )

        game_over = True
        guess_button.config(
            state=tk.DISABLED
        )

        messagebox.showinfo(
            "You Won!",
            f"🎉 Correct!\n\n"
            f"The number was {number}.\n"
            f"Your score: {score}"
        )

    # Guess is low
    elif guess < number:

        score -= 10

        message_label.config(
            text="⬆️ Too Low! Try a Higher Number."
        )

        score_label.config(
            text=f"Score: {score}"
        )

    # Guess is high
    else:

        score -= 10

        message_label.config(
            text="⬇️ Too High! Try a Lower Number."
        )

        score_label.config(
            text=f"Score: {score}"
        )

    # Game Over
    if attempts >= max_attempts and guess != number:

        message_label.config(
            text="😔 Game Over!"
        )

        game_over = True

        guess_button.config(
            state=tk.DISABLED
        )

        messagebox.showinfo(
            "Game Over",
            f"😔 You lost!\n\n"
            f"The correct number was {number}."
        )

    guess_entry.delete(0, tk.END)
    guess_entry.focus()


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Number Guessing Game")

root.geometry("500x600")

root.resizable(False, False)

root.configure(
    bg="#1e1e2f"
)


# ---------------- TITLE ----------------

title_label = tk.Label(
    root,
    text="🎯 NUMBER GUESSING GAME",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="white"
)

title_label.pack(
    pady=25
)


# ---------------- DESCRIPTION ----------------

description = tk.Label(
    root,
    text="Guess the hidden number!",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="lightgray"
)

description.pack()


# ---------------- DIFFICULTY ----------------

difficulty_var = tk.StringVar()

difficulty_var.set("Medium")

difficulty_menu = tk.OptionMenu(
    root,
    difficulty_var,
    "Easy",
    "Medium",
    "Hard"
)

difficulty_menu.config(
    font=("Arial", 13),
    width=15
)

difficulty_menu.pack(
    pady=15
)


# ---------------- INPUT ----------------

guess_entry = tk.Entry(
    root,
    font=("Arial", 20),
    justify="center",
    width=15
)

guess_entry.pack(
    pady=15
)


# ---------------- GUESS BUTTON ----------------

guess_button = tk.Button(
    root,
    text="CHECK GUESS",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    width=18,
    height=2,
    command=check_guess
)

guess_button.pack(
    pady=10
)


# ---------------- MESSAGE ----------------

message_label = tk.Label(
    root,
    text="🎯 Guess the number!",
    font=("Arial", 15, "bold"),
    bg="#1e1e2f",
    fg="yellow"
)

message_label.pack(
    pady=20
)


# ---------------- ATTEMPTS ----------------

attempts_label = tk.Label(
    root,
    text="Attempts: 0 / 7",
    font=("Arial", 13),
    bg="#1e1e2f",
    fg="white"
)

attempts_label.pack(
    pady=5
)


# ---------------- SCORE ----------------

score_label = tk.Label(
    root,
    text="Score: 100",
    font=("Arial", 13, "bold"),
    bg="#1e1e2f",
    fg="cyan"
)

score_label.pack(
    pady=5
)


# ---------------- HISTORY ----------------

history_label = tk.Label(
    root,
    text="Your guesses:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="lightgray"
)

history_label.pack(
    pady=15
)


# ---------------- NEW GAME BUTTON ----------------

new_game_button = tk.Button(
    root,
    text="🔄 NEW GAME",
    font=("Arial", 13, "bold"),
    bg="#2196F3",
    fg="white",
    width=18,
    height=2,
    command=new_game
)

new_game_button.pack(
    pady=10
)


# ---------------- START GAME ----------------

new_game()

root.mainloop()