import json
import os
from datetime import date


DATA_FILE = "data/expenses.json"


class ExpenseManager:

    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(DATA_FILE):
            self.expenses = []
            return

        try:
            with open(DATA_FILE, "r") as file:
                self.expenses = json.load(file)
        except (json.JSONDecodeError, OSError):
            self.expenses = []

    def save_expenses(self):
        os.makedirs("data", exist_ok=True)

        with open(DATA_FILE, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, name, amount, category):
        expense = {
            "id": len(self.expenses) + 1,
            "name": name,
            "amount": amount,
            "category": category,
            "date": str(date.today())
        }

        self.expenses.append(expense)
        self.save_expenses()

        return expense

    def get_expenses(self):
        return self.expenses

    def delete_expense(self, expense_id):
        for expense in self.expenses:
            if expense["id"] == expense_id:
                self.expenses.remove(expense)
                self.save_expenses()
                return True

        return False

    def update_expense(self, expense_id, name, amount, category):
        for expense in self.expenses:
            if expense["id"] == expense_id:
                expense["name"] = name
                expense["amount"] = amount
                expense["category"] = category

                self.save_expenses()
                return True

        return False

    def search_expenses(self, keyword):
        keyword = keyword.lower()

        return [
            expense
            for expense in self.expenses
            if keyword in expense["name"].lower()
        ]

    def filter_by_category(self, category):
        return [
            expense
            for expense in self.expenses
            if expense["category"].lower() == category.lower()
        ]

    def filter_by_date(self, expense_date):
        return [
            expense
            for expense in self.expenses
            if expense["date"] == expense_date
        ]

    def get_total(self):
        return sum(
            expense["amount"]
            for expense in self.expenses
        )

    def get_category_summary(self):
        summary = {}

        for expense in self.expenses:
            category = expense["category"]

            summary[category] = (
                summary.get(category, 0)
                + expense["amount"]
            )

        return summary

    def get_monthly_total(self, year, month):
        total = 0

        for expense in self.expenses:
            expense_date = expense["date"]

            expense_year = int(expense_date[:4])
            expense_month = int(expense_date[5:7])

            if expense_year == year and expense_month == month:
                total += expense["amount"]

        return total
