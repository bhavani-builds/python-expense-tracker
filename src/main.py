import json
import os


DATA_FILE = "data/expenses.json"


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n===== YOUR EXPENSES =====")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['name']} - "
            f"₹{expense['amount']:.2f}"
        )


def delete_expense(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    view_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses(expenses)

            print(
                f"Deleted: {deleted['name']} - "
                f"₹{deleted['amount']:.2f}"
            )
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def show_total(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n==============================")
        print("      PYTHON EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            delete_expense(expenses)

        elif choice == "4":
            show_total(expenses)

        elif choice == "5":
            print("\nThank you for using Python Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
