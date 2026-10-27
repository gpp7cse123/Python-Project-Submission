import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

DB_NAME = "expenses.db"


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("1050x680")
        self.root.minsize(900, 600)
        self.root.configure(bg="#f3f5f9")

        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()

        self.setup_style()
        self.build_ui()
        self.refresh_data()

        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount > 0),
                expense_date TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def setup_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Treeview", rowheight=30, font=("Segoe UI", 10),
                        background="white", fieldbackground="white")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"),
                        background="#e8edf5", foreground="#263248")
        style.configure("TCombobox", padding=6)
        style.configure("TEntry", padding=7)

    def build_ui(self):
        header = tk.Frame(self.root, bg="#172554", height=90)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="Expense Tracker", bg="#172554", fg="white",
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=25, pady=(16, 0))
        tk.Label(header, text="Track your spending • Save smarter",
                 bg="#172554", fg="#c7d2fe",
                 font=("Segoe UI", 10)).pack(anchor="w", padx=27)

        content = tk.Frame(self.root, bg="#f3f5f9")
        content.pack(fill="both", expand=True, padx=22, pady=18)

        cards = tk.Frame(content, bg="#f3f5f9")
        cards.pack(fill="x", pady=(0, 16))
        self.total_value = self.make_card(cards, "ALL-TIME SPENDING", "₹0.00", "#dbeafe")
        self.month_value = self.make_card(cards, "THIS MONTH", "₹0.00", "#dcfce7")
        self.count_value = self.make_card(cards, "TOTAL ENTRIES", "0", "#fef3c7")

        body = tk.Frame(content, bg="#f3f5f9")
        body.pack(fill="both", expand=True)

        form = tk.Frame(body, bg="white", highlightbackground="#e1e7ef",
                        highlightthickness=1, padx=16, pady=16)
        form.pack(side="left", fill="y", padx=(0, 16))
        form.configure(width=280)
        form.pack_propagate(False)

        tk.Label(form, text="Add an expense", bg="white", fg="#172554",
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", pady=(0, 14))

        self.title_var = tk.StringVar()
        self.category_var = tk.StringVar(value="Food")
        self.amount_var = tk.StringVar()
        self.date_var = tk.StringVar(value=date.today().isoformat())

        self.add_field(form, "Expense name", ttk.Entry(form, textvariable=self.title_var))
        self.add_field(form, "Category", ttk.Combobox(
            form, textvariable=self.category_var,
            values=["Food", "Travel", "Shopping", "Education", "Bills",
                    "Health", "Entertainment", "Other"], state="readonly"))
        self.add_field(form, "Amount (₹)", ttk.Entry(form, textvariable=self.amount_var))
        self.add_field(form, "Date (YYYY-MM-DD)", ttk.Entry(form, textvariable=self.date_var))

        tk.Button(form, text="＋  Save Expense", command=self.add_expense,
                  bg="#2563eb", fg="white", activebackground="#1d4ed8",
                  activeforeground="white", relief="flat", cursor="hand2",
                  font=("Segoe UI", 11, "bold"), pady=10).pack(fill="x", pady=(12, 8))

        tk.Label(form, text="Your data is stored locally in expenses.db.",
                 bg="white", fg="#64748b", font=("Segoe UI", 9),
                 wraplength=235, justify="left").pack(anchor="w", pady=(8, 0))

        panel = tk.Frame(body, bg="white", highlightbackground="#e1e7ef",
                         highlightthickness=1, padx=14, pady=14)
        panel.pack(side="left", fill="both", expand=True)

        top = tk.Frame(panel, bg="white")
        top.pack(fill="x", pady=(0, 12))
        tk.Label(top, text="Expense history", bg="white", fg="#172554",
                 font=("Segoe UI", 15, "bold")).pack(side="left")

        tk.Button(top, text="Delete selected", command=self.delete_selected,
                  bg="#fee2e2", fg="#991b1b", activebackground="#fecaca",
                  relief="flat", cursor="hand2", padx=10, pady=6).pack(side="right")

        table_frame = tk.Frame(panel, bg="white")
        table_frame.pack(fill="both", expand=True)

        columns = ("id", "date", "title", "category", "amount")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings",
                                 selectmode="browse")
        headings = {"id": "ID", "date": "DATE", "title": "EXPENSE",
                    "category": "CATEGORY", "amount": "AMOUNT (₹)"}
        widths = {"id": 45, "date": 105, "title": 180, "category": 120, "amount": 110}
        for col in columns:
            self.tree.heading(col, text=headings[col])
            self.tree.column(col, width=widths[col], anchor="w" if col == "title" else "center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.summary_label = tk.Label(panel, text="Category summary will appear here.",
                                      bg="white", fg="#475569",
                                      font=("Segoe UI", 10), anchor="w", justify="left")
        self.summary_label.pack(fill="x", pady=(12, 0))

    def make_card(self, parent, title, value, color):
        card = tk.Frame(parent, bg="white", highlightbackground="#e1e7ef",
                        highlightthickness=1, padx=18, pady=13)
        card.pack(side="left", fill="x", expand=True, padx=(0, 12))
        tk.Label(card, text=title, bg="white", fg="#64748b",
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        value_label = tk.Label(card, text=value, bg="white", fg="#172554",
                               font=("Segoe UI", 21, "bold"))
        value_label.pack(anchor="w", pady=(5, 0))
        return value_label

    def add_field(self, parent, label, widget):
        tk.Label(parent, text=label, bg="white", fg="#334155",
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(7, 5))
        widget.pack(fill="x", pady=(0, 4))

    def add_expense(self):
        title = self.title_var.get().strip()
        category = self.category_var.get().strip()
        amount_text = self.amount_var.get().strip()
        expense_date = self.date_var.get().strip()

        if not title:
            messagebox.showwarning("Missing information", "Please enter an expense name.")
            return

        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Invalid amount", "Enter an amount greater than zero.")
            return

        try:
            date.fromisoformat(expense_date)
        except ValueError:
            messagebox.showwarning("Invalid date", "Use date format YYYY-MM-DD.")
            return

        self.conn.execute(
            "INSERT INTO expenses (title, category, amount, expense_date) VALUES (?, ?, ?, ?)",
            (title, category, amount, expense_date)
        )
        self.conn.commit()

        self.title_var.set("")
        self.amount_var.set("")
        self.date_var.set(date.today().isoformat())
        self.refresh_data()
        messagebox.showinfo("Saved", "Expense saved successfully!")

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select an expense", "Choose an expense from the table first.")
            return

        row = self.tree.item(selected[0], "values")
        if messagebox.askyesno("Confirm delete", f"Delete '{row[2]}' (₹{row[4]})?"):
            self.conn.execute("DELETE FROM expenses WHERE id = ?", (row[0],))
            self.conn.commit()
            self.refresh_data()

    def refresh_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = self.conn.execute(
            "SELECT id, expense_date, title, category, amount "
            "FROM expenses ORDER BY expense_date DESC, id DESC"
        ).fetchall()

        for row in rows:
            self.tree.insert("", "end", values=(
                row[0], row[1], row[2], row[3], f"{row[4]:.2f}"
            ))

        total = self.conn.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses").fetchone()[0]
        month = date.today().strftime("%Y-%m")
        monthly = self.conn.execute(
            "SELECT COALESCE(SUM(amount), 0) FROM expenses WHERE substr(expense_date, 1, 7) = ?",
            (month,)
        ).fetchone()[0]
        count = len(rows)

        self.total_value.config(text=f"₹{total:,.2f}")
        self.month_value.config(text=f"₹{monthly:,.2f}")
        self.count_value.config(text=str(count))

        categories = self.conn.execute(
            "SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC"
        ).fetchall()
        if categories:
            summary = "Category totals:  " + "   •   ".join(
                f"{category}: ₹{amount:,.2f}" for category, amount in categories
            )
        else:
            summary = "Category totals will appear here after you add expenses."
        self.summary_label.config(text=summary)

    def close_app(self):
        self.conn.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
