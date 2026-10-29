# Python Quiz Application (Desktop GUI)

**3rd-Semester Diploma in Computer Science Engineering — Micro-Project**

An interactive, modern desktop quiz application built with **Python 3** and **Tkinter**, using **JSON** for persistent question storage. Designed for college project demonstrations, practical exams, and viva evaluations.

---

## 📁 Project Structure

```text
ayush project/
├── quiz_data.json       # JSON database containing quiz categories and questions
├── quiz_engine.py       # Core logic, OOP models (Question, QuizManager), scoring & file I/O
├── main.py              # Tkinter GUI application (Home, Quiz, Result, and Review screens)
├── README.md            # Quick-start documentation and project guide
└── PROJECT_REPORT.md    # Formal academic micro-project report for diploma submission
```

---

## 🚀 Key Features

1. **Modern Windows GUI**:
   - High-DPI display awareness for ultra-crisp fonts on modern laptops.
   - Elegant Indigo/Slate color scheme with responsive card layouts.
2. **Multiple Quiz Categories**:
   - *Python Programming* (10 Questions)
   - *Computer Fundamentals* (10 Questions)
   - *General Knowledge* (10 Questions)
3. **Interactive Navigation & State Persistence**:
   - Single-question presentation with real-time progress bar.
   - **Previous** and **Next** buttons that preserve chosen answers.
   - **Clear Choice** button to reset selection for the current question.
   - Confirmation dialog if submitting with unanswered questions.
4. **Comprehensive Result Summary**:
   - Total score and percentage calculation.
   - Performance remarks & grade badges (Outstanding, Excellent, Good, Average, Needs Improvement).
   - Stat tiles for Correct, Incorrect, and Skipped questions.
   - **Answer Review Modal**: Shows every question with the user's answer, correct answer, and conceptual explanation.
5. **Robust Error Handling**:
   - Input validation for student name and category selection.
   - Graceful fallback mechanism if `quiz_data.json` is missing or contains invalid syntax.

---

## 🛠️ Requirements & Prerequisites

- **Operating System**: Windows 10 / 11 (also compatible with macOS and Linux)
- **Python**: Python 3.8 or higher (No third-party packages needed; uses built-in `tkinter`, `json`, `os`, `sys`).
- **Editor**: Visual Studio Code (VS Code) or Python IDLE.

---

## 💻 Step-by-Step Instructions to Run in VS Code on Windows

### Step 1: Open the Project in VS Code
1. Launch **Visual Studio Code**.
2. Click **File** > **Open Folder...** (or press `Ctrl + K, Ctrl + O`).
3. Select the folder: `c:\MyProject\Mycreate\ayush project`.

### Step 2: Select Python Interpreter
1. Press `Ctrl + Shift + P` to open the Command Palette.
2. Type `Python: Select Interpreter` and press `Enter`.
3. Select your installed Python version (e.g., Python 3.10 / 3.11 / 3.12 / 3.14).

### Step 3: Run the Application
You can run the application using any of the following methods:

- **Method A (Integrated Terminal)**:
  1. Open the terminal in VS Code: Press `Ctrl + ` `~` (backtick) or select **Terminal** > **New Terminal**.
  2. Type the following command and press `Enter`:
     ```bash
     python main.py
     ```
- **Method B (VS Code Run Button)**:
  1. Click on `main.py` in the File Explorer.
  2. Click the **▷ (Play/Run)** button in the top-right corner of the editor window.

---

## ➕ How to Add New Questions or Categories

All quiz questions are stored in `quiz_data.json`. You can easily add more questions or even create entirely new categories without changing a single line of Python code!

### Adding a New Question to an Existing Category
Open `quiz_data.json` and add an object to the category array:

```json
{
  "id": 11,
  "question": "What is the output of print(type(5)) in Python?",
  "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'number'>"],
  "answer": "<class 'int'>",
  "explanation": "5 is an integer, so Python returns <class 'int'>."
}
```

> **Note**: Make sure options contain 4 choices and the `"answer"` string matches one of the options exactly.

### Adding a New Category
Add a new key under `"categories"` inside `quiz_data.json`:

```json
"categories": {
  "Python Programming": [...],
  "Computer Fundamentals": [...],
  "General Knowledge": [...],
  "Data Structures": [
    {
      "id": 1,
      "question": "Which data structure follows the LIFO (Last In First Out) principle?",
      "options": ["Queue", "Stack", "Linked List", "Tree"],
      "answer": "Stack",
      "explanation": "A stack pushes and pops items from the top (LIFO)."
    }
  ]
}
```

The application will automatically detect and list "Data Structures" in the Home Screen category selector!

---

## 🧠 Python Concepts Demonstrated

| Concept | File / Implementation |
| :--- | :--- |
| **Variables & Data Types** | `int` for counters, `str` for names/options, `float` for percentages, `bool` for checks. |
| **Lists & Dictionaries** | Options lists, categories dictionary, question dictionaries in `quiz_engine.py`. |
| **Conditional Statements** | `if/elif/else` for scoring, input validation, grade remark assignment. |
| **Loops** | `for` loops to iterate through question list, `enumerate` for numbering. |
| **Functions & Methods** | Modular functions for UI event handlers, calculation functions, state resetting. |
| **File Handling & JSON** | `open()` with UTF-8 encoding, `json.load()` for parsing quiz database. |
| **Exception Handling** | `try...except FileNotFoundError, json.JSONDecodeError` with fallback data. |
| **Classes & OOP** | `Question` class (Encapsulation), `QuizManager` class, `QuizApp(tk.Tk)` (Inheritance). |
| **Tkinter GUI** | Frames, Labels, Entry, Radiobuttons, Buttons, Progressbar, Scrollbar, Canvas. |
