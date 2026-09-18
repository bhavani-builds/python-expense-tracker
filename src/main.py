expenses = []


def add_expense():
    name = input("Enter expense name: ")

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
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n===== YOUR EXPENSES =====")

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']} - ₹{expense['amount']:.2f}")


def delete_expense():
    if not expenses:
        print("\nNo expenses found.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"Deleted: {deleted['name']} - ₹{deleted['amount']:.2f}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def show_total():
    if not expenses:
        print("\nNo expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")


def main():
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
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            show_total()

        elif choice == "5":
            print("\nThank you for using Python Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
