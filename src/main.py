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
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
