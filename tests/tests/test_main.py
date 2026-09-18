import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from expense_manager import ExpenseManager


def test_add_expense():
    manager = ExpenseManager()

    manager.expenses = []

    expense = manager.add_expense(
        "Food",
        150,
        "Food"
    )

    assert expense["name"] == "Food"
    assert expense["amount"] == 150
    assert expense["category"] == "Food"


def test_get_total():
    manager = ExpenseManager()

    manager.expenses = [
        {
            "id": 1,
            "name": "Food",
            "amount": 150,
            "category": "Food",
            "date": "2026-09-18"
        },
        {
            "id": 2,
            "name": "Travel",
            "amount": 200,
            "category": "Travel",
            "date": "2026-09-18"
        }
    ]

    assert manager.get_total() == 350


def test_search_expenses():
    manager = ExpenseManager()

    manager.expenses = [
        {
            "id": 1,
            "name": "Food",
            "amount": 150,
            "category": "Food",
            "date": "2026-09-18"
        },
        {
            "id": 2,
            "name": "Bus Ticket",
            "amount": 50,
            "category": "Travel",
            "date": "2026-09-18"
        }
    ]

    results = manager.search_expenses("food")

    assert len(results) == 1
    assert results[0]["name"] == "Food"


def test_filter_by_category():
    manager = ExpenseManager()

    manager.expenses = [
        {
            "id": 1,
            "name": "Food",
            "amount": 150,
            "category": "Food",
            "date": "2026-09-18"
        },
        {
            "id": 2,
            "name": "Bus",
            "amount": 50,
            "category": "Travel",
            "date": "2026-09-18"
        }
    ]

    results = manager.filter_by_category("Food")

    assert len(results) == 1
    assert results[0]["category"] == "Food"


def test_delete_expense():
    manager = ExpenseManager()

    manager.expenses = [
        {
            "id": 1,
            "name": "Food",
            "amount": 150,
            "category": "Food",
            "date": "2026-09-18"
        }
    ]

    result = manager.delete_expense(1)

    assert result is True
    assert len(manager.expenses) == 0


def test_update_expense():
    manager = ExpenseManager()

    manager.expenses = [
        {
            "id": 1,
            "name": "Food",
            "amount": 150,
            "category": "Food",
            "date": "2026-09-18"
        }
    ]

    result = manager.update_expense(
        1,
        "Lunch",
        200,
        "Food"
    )

    assert result is True
    assert manager.expenses[0]["name"] == "Lunch"
    assert manager.expenses[0]["amount"] == 200
