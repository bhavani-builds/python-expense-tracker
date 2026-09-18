from expense_manager import ExpenseManager


def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 75)
    print(f"{'ID':<5}{'NAME':<20}{'AMOUNT':<15}{'CATEGORY':<15}{'DATE':<12}")
    print("=" * 75)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['name'][:18]:<20}"
            f"₹{expense['amount']:<14.2f}"
            f"{expense['category'][:13]:<15}"
            f"{expense['date']:<12}"
        )

    print("=" * 75)


def add_expense(manager):
    print("\n===== ADD EXPENSE =====")

    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input(
        "Enter category (Food/Travel/Education/Shopping/Other): "
    ).strip()

    if not category:
        category = "Other"

    expense = manager.add_expense(name, amount, category)

    print(
        f"\nExpense added successfully!"
        f"\nID: {expense['id']}"
        f"\nName: {expense['name']}"
        f"\nAmount: ₹{expense['amount']:.2f}"
        f"\nCategory: {expense['category']}"
        f"\nDate: {expense['date']}"
    )


def update_expense(manager):
    display_expenses(manager.get_expenses())

    try:
        expense_id = int(input("\nEnter expense ID to update: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    expenses = manager.get_expenses()

    selected = next(
        (expense for expense in expenses if expense["id"] == expense_id),
        None
    )

    if not selected:
        print("Expense not found.")
        return

    name = input(f"Enter new name [{selected['name']}]: ").strip()
    amount_input = input(
        f"Enter new amount [{selected['amount']}]: ₹"
    ).strip()
    category = input(
        f"Enter new category [{selected['category']}]: "
    ).strip()

    if not name:
        name = selected["name"]

    if amount_input:
        try:
            amount = float(amount_input)

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid amount.")
            return
    else:
        amount = selected["amount"]

    if not category:
        category = selected["category"]

    if manager.update_expense(
        expense_id,
        name,
        amount,
        category
    ):
        print("Expense updated successfully!")
    else:
        print("Unable to update expense.")


def delete_expense(manager):
    display_expenses(manager.get_expenses())

    try:
        expense_id = int(input("\nEnter expense ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    if manager.delete_expense(expense_id):
        print("Expense deleted successfully!")
    else:
        print("Expense not found.")


def search_expenses(manager):
    keyword = input("\nEnter expense name to search: ").strip()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = manager.search_expenses(keyword)

    display_expenses(results)


def filter_category(manager):
    category = input("\nEnter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    results = manager.filter_by_category(category)

    display_expenses(results)


def filter_date(manager):
    expense_date = input(
        "\nEnter date (YYYY-MM-DD): "
    ).strip()

    results = manager.filter_by_date(expense_date)

    display_expenses(results)


def show_total(manager):
    total = manager.get_total()

    print(f"\nTotal Expenses: ₹{total:.2f}")


def show_category_summary(manager):
    summary = manager.get_category_summary()

    if not summary:
        print("\nNo expenses found.")
        return

    print("\n===== CATEGORY SUMMARY =====")

    for category, total in summary.items():
        print(f"{category:<15} ₹{total:.2f}")


def show_monthly_total(manager):
    try:
        year = int(input("\nEnter year: "))
        month = int(input("Enter month (1-12): "))

        if month < 1 or month > 12:
            print("Month must be between 1 and 12.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    total = manager.get_monthly_total(year, month)

    print(
        f"\nTotal expenses for {year}-{month:02d}: "
        f"₹{total:.2f}"
    )


def main():
    manager = ExpenseManager()

    while True:
        print("\n")
        print("=" * 40)
        print("       PYTHON EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Filter by Category")
        print("7. Filter by Date")
        print("8. Show Total")
        print("9. Category Summary")
        print("10. Monthly Summary")
        print("11. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(manager)

        elif choice == "2":
            display_expenses(manager.get_expenses())

        elif choice == "3":
            update_expense(manager)

        elif choice == "4":
            delete_expense(manager)

        elif choice == "5":
            search_expenses(manager)

        elif choice == "6":
            filter_category(manager)

        elif choice == "7":
            filter_date(manager)

        elif choice == "8":
            show_total(manager)

        elif choice == "9":
            show_category_summary(manager)

        elif choice == "10":
            show_monthly_total(manager)

        elif choice == "11":
            print("\nThank you for using Python Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please select 1-11.")


if __name__ == "__main__":
    main()
