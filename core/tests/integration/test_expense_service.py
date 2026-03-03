from datetime import date

from core.expense_service import ExpenseService
from core.no_tocar.sqlite_expense_repository import SQLiteExpenseRepository


def create_service():
    repo = SQLiteExpenseRepository()
    repo.empty()
    return ExpenseService(repo)


def test_create_multiple_expenses_and_list():
    service = create_service()

    service.create_expense("Pan", 3, "Mercado", date.today())
    service.create_expense("Leche", 4, "Supermercado", date.today())

    expenses = service.list_expenses()

    titles = [e.title for e in expenses]

    assert len(expenses) == 2
    assert "Pan" in titles
    assert "Leche" in titles


def test_remove_expense_reduces_total():
    service = create_service()

    service.create_expense("Libro", 10, "", date.today())
    service.create_expense("Revista", 5, "", date.today())

    service.remove_expense(1)

    expenses = service.list_expenses()

    assert len(expenses) == 1
    assert expenses[0].title == "Revista"


def test_update_expense_partial_fields():
    service = create_service()

    service.create_expense("Camiseta", 15, "Ropa", date.today())

    service.update_expense(expense_id=1, amount=18)

    expense = service.list_expenses()[0]

    assert expense.title == "Camiseta"
    assert expense.amount == 18
    assert expense.description == "Ropa"


def test_total_amount_after_removal():
    service = create_service()

    service.create_expense("Cursos", 30, "", date.today())
    service.create_expense("Internet", 25, "", date.today())

    assert service.total_amount() == 55

    service.remove_expense(1)

    assert service.total_amount() == 25