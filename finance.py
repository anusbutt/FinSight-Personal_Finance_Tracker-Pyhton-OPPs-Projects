from datetime import datetime
from collections import defaultdict


class Transaction:
    def __init__(self, amount, category, transaction_type, date=None):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = date or datetime.now()

    def __repr__(self):
        return f"{self.transaction_type.title()} of {self.amount} in {self.category} on {self.date.strftime('%Y-%m-%d')}"

class UserFinance:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.transaction_type == "income")
        expense = sum(t.amount for t in self.transactions if t.transaction_type == "expense")
        return income - expense

    def get_expense_by_category(self):
        category_totals = defaultdict(float)
        for t in self.transactions:
            if t.transaction_type == 'expense':
                category_totals[t.category] += t.amount
        return dict(category_totals)

    def get_all_transactions(self):
        return self.transactions
