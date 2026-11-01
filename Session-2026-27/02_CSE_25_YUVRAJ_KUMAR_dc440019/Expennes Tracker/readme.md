
# 💰 Personal Finance Tracker

A desktop-based Personal Finance Tracker developed using Python. This application helps users manage their income, track daily expenses, monitor their remaining balance, and analyze their financial activities through charts and reports.

## 📌 Project Overview

The **Personal Finance Tracker** is a Python-based desktop application designed to make personal money management easier and more organized.

Users can record their income and expenses, categorize transactions, view monthly financial summaries, and visualize their spending patterns through graphical reports.

All transaction data is stored locally using an SQLite database.

## ✨ Features

- **Income Management:** Add and manage different sources of income.
- **Expense Tracking:** Record daily expenses with categories.
- **Monthly Dashboard:** View total income, expenses, and remaining balance.
- **Transaction History:** View all transactions in a structured table.
- **Delete Transactions:** Delete selected transaction records.
- **Category Management:** Organize income and expenses into categories.
- **Charts & Reports:** Visualize expenses using pie charts.
- **Income vs Expenses:** Compare monthly income and expenses using bar charts.
- **Date Filtering:** View financial records for a selected month.
- **SQLite Database:** Store transaction records locally.
- **Input Validation:** Validate transaction amounts and dates.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Graphical User Interface |
| SQLite | Database management |
| Matplotlib | Charts and data visualization |
| ttk | Styled GUI components |
| datetime | Date and time handling |

## 📂 Project Structure

```text
Personal-Finance-Tracker/
│
├── main.py          # Main application and GUI
├── database.py      # Database operations
├── finance.db       # SQLite database (created automatically)
├── requirements.txt # Required Python libraries
└── README.md        # Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the Project Folder

```bash
cd Personal-Finance-Tracker
```

### 3. Install Required Libraries

```bash
pip install matplotlib
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

## 📊 Application Dashboard

The application provides the following financial information:

- Total Income
- Total Expenses
- Remaining Balance
- Number of Transactions

Users can also access charts and reports to understand their financial activities.

## 🗄️ Database

This project uses **SQLite** for local data storage.

The database stores:
- Transaction ID
- Transaction Type
- Transaction Title
- Category
- Amount
- Transaction Date
- Notes

The database file `finance.db` is created automatically when the application initializes the database.

## 🎯 Project Objectives

1. To develop a simple personal finance management system.
2. To understand Python GUI development using Tkinter.
3. To implement database connectivity using SQLite.
4. To understand data visualization using Matplotlib.
5. To improve financial tracking and transaction management.

## 👨‍💻 Project Members

1. **Yuvraj Kumar**
2. **................................**
3. **................................**
4. **................................**
5. **...............................**

## 🚀 Future Improvements

- User login and authentication.
- Export financial reports to PDF or Excel.
- Budget planning and monthly limits.
- Automatic backup and restore.
- Improved graphical dashboard.

## 📜 License

This project is developed for educational and academic purposes.

---

**Developed with ❤️ using Python**
