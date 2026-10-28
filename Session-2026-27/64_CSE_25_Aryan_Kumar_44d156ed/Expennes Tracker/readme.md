
# 💰 Personal Finance Tracker

**A Python-Based Desktop Application for Managing Income and Expenses**

## 📌 About the Project

Personal Finance Tracker is a desktop application developed using Python to help users manage their personal finances efficiently. It allows users to record income and expenses, organize transactions by category, monitor their remaining balance, and analyze financial activities through charts and reports.

The application features a graphical user interface (GUI) built with Tkinter and uses an SQLite database for local data storage.

## ✨ Key Features

- 📊 **Financial Dashboard** — View total income, expenses, remaining balance, and transaction count.
- 💵 **Income Management** — Record salary, pocket money, freelance earnings, gifts, and other income.
- 🛒 **Expense Tracking** — Categorize spending on food, travel, shopping, education, bills, health, and more.
- 📝 **Transaction History** — View saved transactions in a structured table.
- 📅 **Monthly Filtering** — Review financial records for a selected month.
- ➕ **Add Transactions** — Enter transaction type, title, category, amount, date, and optional notes.
- 🗑️ **Delete Transactions** — Remove selected transactions after confirmation.
- 📈 **Charts and Reports** — Visualize expenses by category and compare income with expenses.
- ✅ **Input Validation** — Validate required fields, amounts, dates, and month formats.
- 💾 **Local Storage** — Store financial records in an SQLite database.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Desktop graphical user interface |
| SQLite | Local database management |
| Matplotlib | Financial charts and visual reports |
| ttk | Styled GUI components |
| datetime | Date and time handling |

## 📂 Project Structure

```text
Personal-Finance-Tracker/
│
├── main.py          # Main application and graphical interface
├── database.py      # Database operations and SQL queries
├── finance.db       # Local SQLite database (generated/used by the app)
└── README.md        # Project documentation
```

**Note:** The `finance.db` file may be created when the database module initializes the database. Avoid uploading a database containing private financial records.

## ⚙️ Requirements

- Python 3.10 or later recommended
- Tkinter
- Matplotlib
- SQLite support

Tkinter and SQLite are generally included with standard Python installations. Matplotlib must be installed separately if it is not already available.

## 🚀 Installation and Setup

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

For Windows, enable **Add Python to PATH** during installation.

### Step 2: Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone <YOUR-REPOSITORY-URL>
```

Alternatively, download the repository as a ZIP file and extract it.

### Step 3: Open the Project Folder

Open the project directory in VS Code or another Python editor.

### Step 4: Install Dependencies

Run this command in the terminal:

```bash
python -m pip install matplotlib
```

### Step 5: Run the Application

Execute the following command:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

The Personal Finance Tracker desktop application should open.

## 📖 How to Use

1. Launch the application.
2. Select the desired month using the `YYYY-MM` format.
3. Choose the transaction type: Income or Expense.
4. Enter a transaction title.
5. Select the appropriate category.
6. Enter the amount and transaction date.
7. Add optional notes if needed.
8. Click **Save Transaction** to save the record.
9. View the saved record in the Transaction History table.
10. Select a transaction and click **Delete Selected** to remove it after confirmation.
11. Click **Show Charts** or **View Charts & Reports** to view financial visualizations.

## 📊 Charts and Reports

The application provides financial insights through two visualizations:

### 1. Expense by Category
A pie chart showing how expenses are distributed across different categories for the selected month.

### 2. Income vs Expenses
A bar chart comparing income and expenses over the recent six-month period.

These charts help users understand spending patterns and review their financial activities.

## 🗄️ Database Management

The application uses SQLite to store transaction records locally.

Database operations are organized in `database.py`, while `main.py` manages the interface and user interactions.

The database module is expected to support:

- Adding transactions
- Retrieving transactions for a selected month
- Calculating income, expenses, balance, and transaction count
- Summarizing expenses by category
- Retrieving monthly financial trends
- Deleting transactions

## 🎯 Project Objectives

- Develop a practical desktop finance management application.
- Understand GUI development using Python and Tkinter.
- Learn database connectivity using SQLite.
- Implement transaction management and CRUD operations.
- Apply input validation and exception handling.
- Visualize financial information using Matplotlib.
- Practice modular programming by separating GUI and database code.

## 🎓 Learning Outcomes

Through this project, team members gain practical experience in:

- Python programming fundamentals
- Functions, modules, and exception handling
- GUI design and event handling
- SQLite database operations
- Data validation and transaction management
- Data visualization using Matplotlib
- Software organization and collaborative project development

## 👥 Project Team Members

This project was developed collaboratively by the following team members:

1. **Aryan Kumar**
2. **Arpit Kumar**
3. **Shristi Mehta**
4. **Ankur Kumar**
5. **Neeraj Kumar**

## 🔮 Future Enhancements

- Edit existing transactions.
- Search and filter transactions.
- Set monthly budgets and spending limits.
- Export reports to PDF or CSV.
- Add recurring transactions.
- Introduce data backup and restore functionality.
- Add password protection.
- Improve the dashboard with additional financial insights.

## ⚠️ Current Limitations

- Designed primarily for a single user.
- Data is stored locally on the computer.
- No cloud synchronization or multi-user access.
- Financial reports depend on the accuracy of entered transactions.
- The application does not currently provide a built-in PDF export feature.

## 🔒 Privacy and Data Safety

- Keep the database private if it contains personal financial information.
- Use sample data when demonstrating the project publicly.
- Back up the database periodically to avoid losing financial records.
- Do not commit private financial information to GitHub.

## 📌 Project Information

| Detail | Description |
|---|---|
| Project Name | Personal Finance Tracker |
| Project Type | Desktop Application |
| Programming Language | Python |
| Interface | Tkinter GUI |
| Database | SQLite |
| Visualization | Matplotlib |
| Project Level | Intermediate |
| Purpose | College Project / Academic Submission |
| Team Size | 5 Members |

## 📄 License

This project is intended for educational and academic purposes. Add a suitable license file if you wish to specify the terms under which others may use or distribute the project.

---

**Personal Finance Tracker**  
*Track your income. Manage your expenses. Understand your finances.*
