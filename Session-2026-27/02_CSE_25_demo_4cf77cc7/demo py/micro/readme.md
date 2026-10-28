
# 💰 Personal Finance Tracker

A desktop-based personal finance management application built using Python. It helps users record income, track expenses, monitor their remaining balance, and visualize their financial activity through charts and reports.

## 📌 Project Overview

The Personal Finance Tracker is designed to make everyday money management simple and organized. Users can add income and expense transactions, categorize them, view transaction history, and analyze their financial activities month by month.

The application uses a graphical user interface (GUI) built with Tkinter and stores transaction data locally using an SQLite database.

## ✨ Features

- **Dashboard:** View total income, total expenses, remaining balance, and transaction count.
- **Income Management:** Record salary, pocket money, freelance income, gifts, and other income sources.
- **Expense Tracking:** Categorize expenses such as food, travel, shopping, education, bills, and entertainment.
- **Transaction History:** View recorded transactions in a structured table.
- **Monthly Filter:** View financial records for a selected month.
- **Add Transactions:** Save transaction details, including title, category, amount, date, and optional notes.
- **Delete Transactions:** Remove selected transactions after confirmation.
- **Charts and Reports:** Visualize expenses by category and compare income versus expenses across months.
- **Input Validation:** Validate transaction amounts, dates, and required fields.
- **Local Data Storage:** Save financial records in an SQLite database on your computer.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Desktop graphical user interface |
| SQLite | Local database storage |
| Matplotlib | Charts and financial reports |
| ttk | Styled interface components |
| datetime | Date and month handling |

## 📂 Project Structure

```text
Personal-Finance-Tracker/
│
├── main.py          # Main application and GUI
├── database.py      # Database operations and queries
├── finance.db       # SQLite database, created or used by the application
└── README.md        # Project documentation
```

**Note:** `finance.db` is the database filename referenced by the application. The database file may be created automatically by `database.py`, depending on its implementation. Do not upload a database containing private financial information.

## ⚙️ Requirements

- Python 3.10 or later recommended
- Tkinter (usually included with standard Python installations)
- Matplotlib
- SQLite support (included with standard Python installations)

## 🚀 Installation and Setup

### 1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

During installation on Windows, enable **Add Python to PATH**.

### 2. Download or Clone the Repository

Clone the repository using Git:

```bash
git clone <YOUR-REPOSITORY-URL>
```

Alternatively, download the repository as a ZIP file and extract it.

### 3. Open the Project Folder

Open a terminal or PowerShell window in the project directory.

### 4. Install Dependencies

Install Matplotlib using:

```bash
python -m pip install matplotlib
```

If your system uses the `py` launcher, you can use:

```bash
py -m pip install matplotlib
```

### 5. Run the Application

Run the following command from the project directory:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

The Personal Finance Tracker desktop window should open.

## 📖 How to Use

1. Launch the application.
2. Select the month you want to view using the `YYYY-MM` format.
3. Choose the transaction type: Income or Expense.
4. Enter the transaction title and select a category.
5. Enter the amount and transaction date.
6. Add optional notes if required.
7. Click **Save Transaction** to store the record.
8. View your transactions in the Transaction History table.
9. Select a transaction and click **Delete Selected** to remove it after confirmation.
10. Click **Show Charts** or **View Charts & Reports** to analyze your financial data.

### Example

| Transaction Type | Title | Category | Amount |
|---|---|---|---:|
| Income | Monthly Pocket Money | Pocket Money | ₹3,000 |
| Expense | Books | Education | ₹500 |
| Expense | Bus Fare | Travel | ₹300 |

Example remaining balance: ₹2,200.

*These are sample transactions for demonstration purposes.*

## 📊 Reports and Visualization

The application provides two types of financial visualization:

- **Expense by Category:** A pie chart showing how expenses are distributed across categories for the selected month.
- **Income vs Expenses:** A bar chart comparing monthly income and expenses over the recent six-month period.

These reports help users understand their spending patterns and review their financial activity.

## 🗄️ Database

The application uses SQLite for local data storage.

The database operations are handled separately in `database.py`, keeping the database logic separate from the user interface in `main.py`.

The application expects database functions for:

- Adding a transaction
- Retrieving transactions for a selected month
- Calculating monthly income, expenses, balance, and transaction count
- Summarizing expenses by category
- Retrieving monthly income and expense trends
- Deleting a transaction

## 🎯 Project Objectives

- To develop a user-friendly desktop finance management application.
- To understand GUI development using Python and Tkinter.
- To learn database connectivity using SQLite.
- To apply data validation and CRUD operations.
- To visualize financial data using charts.
- To improve practical programming and problem-solving skills.

## 🎓 Learning Outcomes

Through this project, students can learn:

- Python functions, variables, modules, and exception handling.
- Desktop GUI development.
- Database integration and SQL operations.
- Input validation and data management.
- Data visualization with Matplotlib.
- Organizing a Python project into separate modules.

## 🔮 Future Enhancements

- Edit existing transactions.
- Search and filter transactions by category or date.
- Set monthly budgets and spending limits.
- Export financial reports to CSV or PDF.
- Add recurring transactions.
- Add a dashboard with more detailed financial insights.
- Implement optional password protection and data backup.

## ⚠️ Limitations

- The current application is designed for a single user.
- Data is stored locally rather than in an online database.
- Financial summaries depend on the transactions entered by the user.
- The current interface does not include cloud synchronization or multi-user access.

## 🔒 Privacy Notice

The application is intended for personal financial record-keeping. Keep your database file private if it contains real financial information. Before sharing the project publicly, use sample data or remove personal records.

## 👨‍💻 Project Information

- **Project Name:** Personal Finance Tracker
- **Project Type:** Python Desktop Application
- **Project Level:** Intermediate
- **Purpose:** College Project / Academic Submission
- **Storage:** SQLite Database
- **Interface:** Tkinter GUI

## 📄 License

This project is intended for educational and learning purposes. If you plan to distribute or reuse it, add a suitable license to the repository.

---

**Personal Finance Tracker** — Manage your income, track your expenses, and understand your money better.
