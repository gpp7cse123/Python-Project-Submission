import sqlite3
from datetime import date

DB_NAME = "finance.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kind TEXT NOT NULL
                    CHECK(kind IN ('Income', 'Expense')),
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount > 0),
                transaction_date TEXT NOT NULL,
                notes TEXT DEFAULT ''
            )
        """)


def add_transaction(kind, title, category, amount, tx_date, notes=""):
    if kind not in ("Income", "Expense"):
        raise ValueError("Invalid transaction type.")

    if not title.strip() or not category.strip():
        raise ValueError("Title and category are required.")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    date.fromisoformat(tx_date)

    with get_connection() as conn:
        conn.execute("""
            INSERT INTO transactions
            (kind, title, category, amount, transaction_date, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            kind, title.strip(), category.strip(),
            amount, tx_date, notes.strip()
        ))


def get_transactions(month=None):
    with get_connection() as conn:
        if month:
            return conn.execute("""
                SELECT id, kind, title, category,
                       amount, transaction_date, notes
                FROM transactions
                WHERE substr(transaction_date, 1, 7) = ?
                ORDER BY transaction_date DESC, id DESC
            """, (month,)).fetchall()

        return conn.execute("""
            SELECT id, kind, title, category,
                   amount, transaction_date, notes
            FROM transactions
            ORDER BY transaction_date DESC, id DESC
        """).fetchall()


def delete_transaction(transaction_id):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM transactions WHERE id = ?",
            (int(transaction_id),)
        )


def get_month_summary(month):
    with get_connection() as conn:
        income = conn.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE kind = 'Income'
            AND substr(transaction_date, 1, 7) = ?
        """, (month,)).fetchone()[0]

        expenses = conn.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE kind = 'Expense'
            AND substr(transaction_date, 1, 7) = ?
        """, (month,)).fetchone()[0]

        count = conn.execute("""
            SELECT COUNT(*)
            FROM transactions
            WHERE substr(transaction_date, 1, 7) = ?
        """, (month,)).fetchone()[0]

    return {
        "income": income,
        "expenses": expenses,
        "balance": income - expenses,
        "count": count
    }


def get_category_summary(month):
    with get_connection() as conn:
        return conn.execute("""
            SELECT category, SUM(amount)
            FROM transactions
            WHERE kind = 'Expense'
            AND substr(transaction_date, 1, 7) = ?
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """, (month,)).fetchall()


def get_monthly_trend(month_count=6):
    from datetime import datetime

    today = date.today()
    results = []

    for offset in range(month_count - 1, -1, -1):
        index = today.year * 12 + today.month - 1 - offset
        year = index // 12
        month_num = index % 12 + 1

        month = f"{year:04d}-{month_num:02d}"
        label = datetime(year, month_num, 1).strftime("%b %Y")
        summary = get_month_summary(month)

        results.append({
            "label": label,
            "income": summary["income"],
            "expenses": summary["expenses"]
        })

    return results


# Automatically create database table.
create_tables()