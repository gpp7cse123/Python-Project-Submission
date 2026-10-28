
# 🧾 Python Billing System – Invoice Generator

A simple, console-based billing application developed using Python. It allows users to enter customer details, add multiple items with their prices and quantities, calculate the grand total, and generate a formatted invoice with the current date and time.

## 📌 Project Overview

The Python Billing System is designed to simplify the billing process for small shops and businesses. It automatically calculates the total price of each item and the final bill amount based on the entered price and quantity.

The generated invoice displays customer information, item details, individual totals, the grand total, and a thank-you message.

## ✨ Features

- **Customer Details:** Enter the customer's name and phone number.
- **Default Values:** Uses "Valued Customer" if the name is left blank and "N/A" if the phone number is left blank.
- **Multiple Items:** Add multiple products to a single bill.
- **Automatic Calculation:** Calculates each item's total using price × quantity.
- **Grand Total:** Calculates the total cost of all items.
- **Date and Time:** Displays the current date and time on the invoice.
- **Re-enter Item:** Type `re` in the item price field to skip the current item and start again.
- **Exit Option:** Press Enter when prompted to confirm exiting after leaving the item name blank.
- **Formatted Invoice:** Prints a neatly structured invoice in the terminal.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| `datetime` module | Retrieves and formats the current date and time |
| Lists and Dictionaries | Store item and billing details |
| `input()` and `print()` | Accept input and display the invoice |
| f-strings | Format invoice output |

## 📂 Project Structure

```text
Python-Billing-System/
│
├── main.py       # Main billing application
└── README.md     # Project documentation
```

## ⚙️ Requirements

- Python 3.8 or later recommended
- A code editor such as VS Code or IDLE
- A terminal or command prompt

**External libraries are not required.** The project uses Python's built-in `datetime` module.

## 🚀 Installation and Setup

### 1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

On Windows, select **Add Python to PATH** during installation.

### 2. Download or Clone the Repository

Clone the repository:

```bash
git clone <YOUR-REPOSITORY-URL>
```

Alternatively, download the repository as a ZIP file and extract it.

### 3. Open the Project Folder

Open the project folder in VS Code or your preferred Python editor.

### 4. Run the Program

Open the terminal in the project directory and execute:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## 📖 How to Use

1. Run the Python program.
2. Enter the customer name.
3. Enter the customer phone number.
4. Enter the item name.
5. Enter the item's price in rupees.
6. Enter the quantity.
7. Repeat the process to add more items.
8. To finish entering items, leave the item name blank and confirm exit by pressing Enter or typing `y`.
9. View the generated invoice in the terminal.

### Special Commands

| Input | Action |
|---|---|
| Leave customer name blank | Uses "Valued Customer" |
| Leave phone number blank | Uses "N/A" |
| Type `re` in the item price field | Skips the current item and restarts item entry |
| Leave item name blank, then press Enter or type `y` | Exits item entry |
| Leave item name blank, then type `n` | Continues item entry |

## 💡 Example

Suppose a customer purchases the following items:

| Item | Price | Quantity | Total |
|---|---:|---:|---:|
| Notebook | ₹50.00 | 2 | ₹100.00 |
| Pen | ₹10.00 | 5 | ₹50.00 |
| School Bag | ₹500.00 | 1 | ₹500.00 |
| **Grand Total** | | | **₹650.00** |

The program generates an invoice containing the customer details, date, time, itemized list, grand total, and a thank-you message.

*The values above are for demonstration purposes.*

## 🎯 Project Objectives

- To develop a basic billing application using Python.
- To automate item-wise and total bill calculations.
- To understand user input and output operations.
- To practice lists, dictionaries, loops, conditional statements, and functions.
- To learn string formatting using f-strings.
- To generate a structured invoice in the terminal.

## 🎓 Learning Outcomes

By developing this project, students can learn:

- Python fundamentals and program flow.
- Using loops and conditional statements.
- Working with lists and dictionaries.
- Performing arithmetic calculations.
- Handling date and time with the `datetime` module.
- Formatting text for readable terminal output.
- Building a practical, real-world console application.

## 🔮 Future Enhancements

- Save invoices automatically as text files or PDF documents.
- Add a graphical user interface using Tkinter.
- Store customer and transaction records in an SQLite database.
- Add discounts, GST, and tax calculations.
- Validate price and quantity inputs.
- Add product inventory management.
- Generate unique invoice numbers.
- Add search and billing history features.

## ⚠️ Limitations

- The current application runs in the terminal.
- Invoices are displayed on the screen and are not automatically saved.
- Billing records are not stored in a database.
- The program does not currently include GST, discounts, or inventory management.
- Price and quantity inputs are not fully validated against invalid values.

## 👨‍💻 Project Information

- **Project Name:** Python Billing System – Invoice Generator
- **Project Type:** Console-Based Application
- **Programming Language:** Python
- **Level:** Beginner
- **Purpose:** Learning / College Project
- **External Dependencies:** None

## 📄 License

This project is intended for educational purposes. Add an appropriate license file if you wish to distribute or reuse the project under specific terms.

---

**Python Billing System** — Simple billing, automatic calculations, and clear invoices.
