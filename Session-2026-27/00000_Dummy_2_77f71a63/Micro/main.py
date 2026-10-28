import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

import database as db

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ---------- COLORS ----------
BG = "#F1F5F9"
WHITE = "#FFFFFF"
NAVY = "#172554"
BLUE = "#2563EB"
GREEN = "#15803D"
RED = "#B91C1C"
TEXT = "#1E293B"
MUTED = "#64748B"
BORDER = "#E2E8F0"

INCOME_CATEGORIES = [
    "Salary", "Pocket Money", "Freelance",
    "Business", "Gift", "Other Income"
]

EXPENSE_CATEGORIES = [
    "Food", "Travel", "Shopping", "Education",
    "Bills", "Health", "Entertainment", "Rent", "Other"
]


# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("1180x740")
root.minsize(980, 620)
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=WHITE,
    fieldbackground=WHITE,
    foreground=TEXT,
    rowheight=30,
    font=("Segoe UI", 10)
)

style.configure(
    "Treeview.Heading",
    background="#E2E8F0",
    foreground=NAVY,
    font=("Segoe UI", 10, "bold")
)


# ---------- HEADER ----------
header = tk.Frame(root, bg=NAVY, height=85)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="PERSONAL FINANCE TRACKER",
    bg=NAVY,
    fg=WHITE,
    font=("Segoe UI", 22, "bold")
).pack(anchor="w", padx=24, pady=(10, 0))

tk.Label(
    header,
    text="Manage income • Track expenses • Grow your savings",
    bg=NAVY,
    fg="#CBD5E1",
    font=("Segoe UI", 10)
).pack(anchor="w", padx=27)


# ---------- CONTENT ----------
content = tk.Frame(root, bg=BG)
content.pack(fill="both", expand=True, padx=20, pady=15)


# ---------- MONTH FILTER ----------
toolbar = tk.Frame(content, bg=BG)
toolbar.pack(fill="x", pady=(0, 12))

month_var = tk.StringVar(value=date.today().strftime("%Y-%m"))

tk.Label(
    toolbar,
    text="Selected Month:",
    bg=BG,
    fg=TEXT,
    font=("Segoe UI", 10, "bold")
).pack(side="left", padx=(0, 8))

ttk.Entry(
    toolbar,
    textvariable=month_var,
    width=12
).pack(side="left")

tk.Label(
    toolbar,
    text="(YYYY-MM)",
    bg=BG,
    fg=MUTED
).pack(side="left", padx=5)


# ---------- SUMMARY CARDS ----------
cards = tk.Frame(content, bg=BG)
cards.pack(fill="x", pady=(0, 14))


def make_card(title, color):
    card = tk.Frame(
        cards,
        bg=WHITE,
        padx=14,
        pady=12,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    card.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 10)
    )

    tk.Label(
        card,
        text=title,
        bg=WHITE,
        fg=MUTED,
        font=("Segoe UI", 9, "bold")
    ).pack(anchor="w")

    value = tk.Label(
        card,
        text="₹0.00",
        bg=WHITE,
        fg=color,
        font=("Segoe UI", 19, "bold")
    )

    value.pack(anchor="w", pady=(6, 0))
    return value


income_label = make_card("TOTAL INCOME", GREEN)
expense_label = make_card("TOTAL EXPENSES", RED)
balance_label = make_card("REMAINING BALANCE", BLUE)
count_label = make_card("TRANSACTIONS", NAVY)


# ---------- MAIN TWO-COLUMN AREA ----------
body = tk.Frame(content, bg=BG)
body.pack(fill="both", expand=True)

form = tk.Frame(
    body,
    bg=WHITE,
    width=270,
    padx=15,
    pady=15,
    highlightbackground=BORDER,
    highlightthickness=1
)

form.pack(side="left", fill="y", padx=(0, 14))
form.pack_propagate(False)

right = tk.Frame(
    body,
    bg=WHITE,
    padx=12,
    pady=12,
    highlightbackground=BORDER,
    highlightthickness=1
)

right.pack(side="left", fill="both", expand=True)


# ---------- INPUT FORM ----------
tk.Label(
    form,
    text="Add Transaction",
    bg=WHITE,
    fg=NAVY,
    font=("Segoe UI", 15, "bold")
).pack(anchor="w", pady=(0, 10))

kind_var = tk.StringVar(value="Expense")
title_var = tk.StringVar()
category_var = tk.StringVar(value="Food")
amount_var = tk.StringVar()
date_var = tk.StringVar(value=date.today().isoformat())
notes_var = tk.StringVar()


def add_field(label, widget):
    tk.Label(
        form,
        text=label,
        bg=WHITE,
        fg=TEXT,
        font=("Segoe UI", 10, "bold")
    ).pack(anchor="w", pady=(7, 4))

    widget.pack(fill="x")


def change_categories(*args):
    if kind_var.get() == "Income":
        options = INCOME_CATEGORIES
        default = "Salary"
    else:
        options = EXPENSE_CATEGORIES
        default = "Food"

    category_box["values"] = options

    if category_var.get() not in options:
        category_var.set(default)


add_field(
    "Transaction Type",
    ttk.Combobox(
        form,
        textvariable=kind_var,
        values=["Income", "Expense"],
        state="readonly"
    )
)

kind_var.trace_add("write", change_categories)

add_field(
    "Title",
    ttk.Entry(form, textvariable=title_var)
)

category_box = ttk.Combobox(
    form,
    textvariable=category_var,
    values=EXPENSE_CATEGORIES,
    state="readonly"
)

add_field("Category", category_box)

add_field(
    "Amount (₹)",
    ttk.Entry(form, textvariable=amount_var)
)

add_field(
    "Date (YYYY-MM-DD)",
    ttk.Entry(form, textvariable=date_var)
)

add_field(
    "Notes (Optional)",
    ttk.Entry(form, textvariable=notes_var)
)


# ---------- TRANSACTION TABLE ----------
tk.Label(
    right,
    text="Transaction History",
    bg=WHITE,
    fg=NAVY,
    font=("Segoe UI", 15, "bold")
).pack(anchor="w", pady=(0, 10))

columns = (
    "id", "type", "title",
    "category", "amount", "date"
)

tree = ttk.Treeview(
    right,
    columns=columns,
    show="headings",
    selectmode="browse"
)

headings = {
    "id": "ID",
    "type": "TYPE",
    "title": "TITLE",
    "category": "CATEGORY",
    "amount": "AMOUNT",
    "date": "DATE"
}

widths = {
    "id": 35,
    "type": 75,
    "title": 130,
    "category": 95,
    "amount": 95,
    "date": 95
}

for col in columns:
    tree.heading(col, text=headings[col])
    tree.column(
        col,
        width=widths[col],
        anchor="w" if col == "title" else "center"
    )

tree.tag_configure("Income", foreground=GREEN)
tree.tag_configure("Expense", foreground=RED)

scrollbar = ttk.Scrollbar(
    right,
    orient="vertical",
    command=tree.yview
)

tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# ---------- VALIDATE MONTH ----------
def valid_month(value):
    try:
        parsed = datetime.strptime(value, "%Y-%m")
        return parsed.strftime("%Y-%m") == value
    except ValueError:
        return False


# ---------- REFRESH DASHBOARD ----------
def refresh_dashboard(show_error=True):
    month = month_var.get().strip()

    if not valid_month(month):
        if show_error:
            messagebox.showerror(
                "Invalid Month",
                "Enter month in YYYY-MM format, e.g. 2026-10."
            )
        return

    summary = db.get_month_summary(month)

    income_label.config(
        text=f"₹{summary['income']:,.2f}"
    )

    expense_label.config(
        text=f"₹{summary['expenses']:,.2f}"
    )

    balance = summary["balance"]

    balance_label.config(
        text=f"₹{balance:,.2f}",
        fg=GREEN if balance >= 0 else RED
    )

    count_label.config(text=str(summary["count"]))

    for item in tree.get_children():
        tree.delete(item)

    for row in db.get_transactions(month):
        tx_id, kind, title, category, amount, tx_date, notes = row

        tree.insert(
            "",
            "end",
            values=(
                tx_id,
                kind,
                title,
                category,
                f"{amount:,.2f}",
                tx_date
            ),
            tags=(kind,)
        )


# ---------- SAVE TRANSACTION ----------
def save_transaction():
    kind = kind_var.get()
    title = title_var.get().strip()
    category = category_var.get().strip()
    amount_text = amount_var.get().strip()
    tx_date = date_var.get().strip()
    notes = notes_var.get().strip()

    if not title:
        messagebox.showwarning(
            "Missing Title",
            "Please enter a transaction title."
        )
        return

    try:
        amount = float(amount_text)

        if amount <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Amount",
            "Enter an amount greater than zero."
        )
        return

    try:
        date.fromisoformat(tx_date)
    except ValueError:
        messagebox.showerror(
            "Invalid Date",
            "Enter a valid date in YYYY-MM-DD format."
        )
        return

    try:
        db.add_transaction(
            kind,
            title,
            category,
            amount,
            tx_date,
            notes
        )

        title_var.set("")
        amount_var.set("")
        notes_var.set("")
        date_var.set(date.today().isoformat())

        month_var.set(tx_date[:7])
        refresh_dashboard()

        messagebox.showinfo(
            "Success",
            f"{kind} saved successfully!"
        )

    except (ValueError, Exception) as error:
        messagebox.showerror("Database Error", str(error))


# ---------- DELETE TRANSACTION ----------
def delete_selected():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select a transaction first."
        )
        return

    values = tree.item(selected[0], "values")

    if messagebox.askyesno(
        "Confirm Delete",
        f"Delete '{values[2]}' for ₹{values[4]}?"
    ):
        try:
            db.delete_transaction(values[0])
            refresh_dashboard()

        except Exception as error:
            messagebox.showerror("Delete Error", str(error))


# ---------- CHARTS AND REPORTS ----------
def show_charts():
    month = month_var.get().strip()

    if not valid_month(month):
        messagebox.showerror(
            "Invalid Month",
            "Enter month as YYYY-MM."
        )
        return

    categories = db.get_category_summary(month)
    trend = db.get_monthly_trend(6)
    summary = db.get_month_summary(month)

    window = tk.Toplevel(root)
    window.title("Finance Charts and Reports")
    window.geometry("1000x620")
    window.configure(bg=BG)

    tk.Label(
        window,
        text=f"Charts & Reports — {month}",
        bg=BG,
        fg=NAVY,
        font=("Segoe UI", 18, "bold")
    ).pack(anchor="w", padx=18, pady=12)

    figure = Figure(figsize=(10, 5), dpi=100)

    pie_ax = figure.add_subplot(121)
    bar_ax = figure.add_subplot(122)

    if categories:
        labels = [item[0] for item in categories]
        amounts = [item[1] for item in categories]

        pie_ax.pie(
            amounts,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )
        pie_ax.set_title("Expense by Category")
    else:
        pie_ax.text(
            0.5, 0.5, "No expenses this month",
            ha="center", va="center"
        )
        pie_ax.set_title("Expense by Category")
        pie_ax.axis("off")

    labels = [item["label"] for item in trend]
    incomes = [item["income"] for item in trend]
    expenses = [item["expenses"] for item in trend]

    positions = list(range(len(labels)))
    width = 0.36

    bar_ax.bar(
        [p - width / 2 for p in positions],
        incomes,
        width,
        label="Income"
    )

    bar_ax.bar(
        [p + width / 2 for p in positions],
        expenses,
        width,
        label="Expenses"
    )

    bar_ax.set_xticks(positions)
    bar_ax.set_xticklabels(labels, rotation=35, ha="right")
    bar_ax.set_title("Income vs Expenses")
    bar_ax.set_ylabel("Amount (₹)")
    bar_ax.legend()
    bar_ax.grid(axis="y", alpha=0.25)

    figure.tight_layout()

    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(
        fill="both", expand=True, padx=12, pady=8
    )

    tk.Label(
        window,
        text=(
            f"Income: ₹{summary['income']:,.2f}     "
            f"Expenses: ₹{summary['expenses']:,.2f}     "
            f"Balance: ₹{summary['balance']:,.2f}"
        ),
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 11, "bold")
    ).pack(pady=10)


# ---------- BUTTONS ----------
tk.Button(
    form,
    text="+ Save Transaction",
    command=save_transaction,
    bg=BLUE,
    fg=WHITE,
    activebackground="#1D4ED8",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    font=("Segoe UI", 11, "bold"),
    pady=10
).pack(fill="x", pady=(15, 7))

tk.Button(
    form,
    text="Delete Selected",
    command=delete_selected,
    bg="#FEE2E2",
    fg=RED,
    activebackground="#FECACA",
    relief="flat",
    cursor="hand2",
    pady=9
).pack(fill="x", pady=5)

tk.Button(
    form,
    text="View Charts & Reports",
    command=show_charts,
    bg="#DCFCE7",
    fg=GREEN,
    activebackground="#BBF7D0",
    relief="flat",
    cursor="hand2",
    pady=9
).pack(fill="x", pady=5)

tk.Label(
    form,
    text=(
        "Income increases your balance.\n"
        "Expenses reduce your balance.\n\n"
        "Your data is saved in finance.db."
    ),
    bg=WHITE,
    fg=MUTED,
    justify="left",
    font=("Segoe UI", 9)
).pack(anchor="w", pady=(14, 0))


# ---------- TOOLBAR BUTTONS ----------
tk.Button(
    toolbar,
    text="Refresh",
    command=refresh_dashboard,
    bg="#DBEAFE",
    fg=NAVY,
    relief="flat",
    cursor="hand2",
    padx=12,
    pady=5
).pack(side="right", padx=5)

tk.Button(
    toolbar,
    text="Show Charts",
    command=show_charts,
    bg=BLUE,
    fg=WHITE,
    relief="flat",
    cursor="hand2",
    padx=12,
    pady=5
).pack(side="right", padx=5)


# ---------- START APP ----------
refresh_dashboard(show_error=False)
root.mainloop()