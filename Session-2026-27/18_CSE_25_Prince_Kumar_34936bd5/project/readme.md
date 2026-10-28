
# 🎯 Number Guessing Game

## 📌 Project Overview

The **Number Guessing Game** is a simple GUI-based game developed using Python and the Tkinter library. In this game, the computer randomly selects a hidden number, and the player has to guess the correct number within a limited number of attempts.

The game provides hints such as **"Too Low"** and **"Too High"** to help the player find the correct number. It also includes a scoring system, guess history, difficulty levels, and a New Game option.

## 🎯 Objectives

- To develop an interactive game using Python.
- To understand the use of the Tkinter GUI library.
- To generate random numbers using the `random` module.
- To implement conditional statements and functions.
- To manage attempts and scores.
- To create a simple and user-friendly graphical interface.

## ✨ Features

- **Three Difficulty Levels:** Easy, Medium, and Hard.
- **Random Number Generation:** The computer selects a random number for every new game.
- **Limited Attempts:** Players have a fixed number of guesses.
- **Instant Feedback:** The game indicates whether the guess is too high or too low.
- **Scoring System:** Players start with 100 points and lose 10 points for each incorrect guess. Bonus points are awarded for guessing correctly.
- **Guess History:** Displays the numbers already guessed by the player.
- **Game Over Notification:** Displays a message when the player wins or runs out of attempts.
- **New Game Option:** Allows the player to restart the game.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **GUI Library:** Tkinter
- **Random Number Generation:** Python `random` module
- **Message Dialogs:** Tkinter `messagebox`
- **Code Editor:** Visual Studio Code or any Python-compatible editor

## 🎮 Difficulty Levels

| Level | Number Range | Maximum Attempts |
|---|---|---:|
| Easy | 1–50 | 10 |
| Medium | 1–100 | 7 |
| Hard | 1–500 | 6 |

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md
```

**File descriptions:**

- `number_guessing_game.py` — Contains the complete Python source code.
- `README.md` — Contains the project description, features, and instructions.

## ⚙️ Requirements

Before running the project, make sure Python 3 is installed on your computer.

The project uses the following modules:

- `tkinter` — To create the graphical user interface.
- `random` — To generate a random number.

These modules are included with most standard Python installations. No external Python packages are normally required.

## 🚀 Installation and Execution

### Step 1: Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

During installation on Windows, enable **Add Python to PATH** if that option is available.

### Step 2: Save the Source Code

Save the provided Python code in a file named:

`number_guessing_game.py`

### Step 3: Open the Project

Open the project folder in Visual Studio Code or another Python editor.

### Step 4: Run the Program

Open the terminal in the project folder and execute:

```bash
python number_guessing_game.py
```

On some systems, you may need to use:

```bash
python3 number_guessing_game.py
```

### Step 5: Start Playing

The game window will open. Select a difficulty level and click **NEW GAME** if you want to start a fresh round.

## 🕹️ How to Play

1. Open the Number Guessing Game.
2. Select Easy, Medium, or Hard.
3. Click **NEW GAME** to start a round.
4. Enter a number within the selected range.
5. Click **CHECK GUESS**.
6. Read the feedback displayed on the screen.
7. Continue guessing until you find the correct number or use all available attempts.
8. Check your score and guess history.
9. Click **NEW GAME** to play again.

## 🧠 Working Principle

The game works through the following steps:

1. The program generates a random integer according to the selected difficulty.
2. The number of attempts and the initial score are reset.
3. The player enters a guess in the input field.
4. The program validates the input and checks whether it is within the permitted range.
5. The guess is compared with the hidden number.
6. If the guess is too low, the program asks the player to try a higher number.
7. If the guess is too high, the program asks the player to try a lower number.
8. If the guess is correct, the player wins and receives bonus points based on the remaining attempts.
9. If the maximum number of attempts is reached, the game ends and displays the correct number.

## 📊 Scoring System

- Initial score: **100 points**
- Penalty for each incorrect guess: **10 points**
- Bonus for a correct guess: **10 points for each unused attempt**

The bonus is calculated using:

```python
bonus = (max_attempts - attempts) * 10
```

The final score is calculated by adding the bonus to the score remaining after incorrect guesses.

## 📚 Python Concepts Used

- Variables and data types
- Global variables
- Functions
- Conditional statements (`if`, `elif`, `else`)
- Exception handling (`try` and `except`)
- Random number generation
- Tkinter labels, buttons, entry fields, and option menus
- Event-driven programming
- Message boxes
- String formatting using f-strings

## 🔍 Input Validation

The game checks the player's input before comparing it with the hidden number.

- Accepts valid integer input.
- Displays a warning if the input is not a valid number.
- Checks whether the number is within the selected difficulty range.
- Does not count invalid or out-of-range inputs as attempts.

## ⚠️ Limitations

- The game is designed for a single player.
- The game runs locally on a computer.
- Scores are not saved permanently.
- The game does not maintain a leaderboard or player profile.
- The player must start a new game manually after a round ends.

## 🔮 Future Enhancements

The project can be improved by adding:

- Sound effects and background music.
- A timer to measure playing time.
- A high-score system.
- A leaderboard for multiple players.
- A restart confirmation option.
- A more advanced graphical interface.

## 🎓 Learning Outcomes

Through this project, I learned how to develop a graphical application using Python and Tkinter. I also learned how to generate random numbers, handle user input, use conditional statements, manage game states, and implement a scoring system.

## 🏁 Conclusion

The Number Guessing Game is a beginner-friendly Python project that combines programming logic with a graphical user interface. It provides an interactive way to practice Python concepts while developing problem-solving skills. The project demonstrates the practical use of functions, random numbers, event handling, and conditional statements in a simple game application.

## 👨‍💻 Author

**Project Name:** Number Guessing Game  
**Language:** Python  
**Project Type:** Mini Project  
**Interface:** Tkinter GUI

---

⭐ If you find this project useful, you can improve it by adding new features and customizing its design.
