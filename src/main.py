expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\nYour Expenses:")

    for expense in expenses:
        print(f"{expense['name']} - ₹{expense['amount']}")
        def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"Deleted: {deleted['name']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

      elif choice == "3":
    delete_expense()

elif choice == "4":
    print("Thank you for using Expense Tracker!")
    break


if __name__ == "__main__":
    main()
