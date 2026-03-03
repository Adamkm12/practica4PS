from datetime import date
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from core.expense_service import ExpenseService
from core.in_memory_expense_repository import InMemoryExpenseRepository


# Carga los escenarios definidos en el archivo .feature
scenarios("./expense_management.feature")


# Fixture de contexto compartido entre steps
@pytest.fixture
def context():
    repo = InMemoryExpenseRepository()
    service = ExpenseService(repo)
    return {"service": service, "db": repo}


@given(parsers.parse("un gestor de gastos vacío"))
def empty_manager(context):
    pass


@given(parsers.parse("un gestor con un gasto de {amount:d} euros"))
def manager_with_one_expense(context, amount):
    # Se crea un gasto inicial para los escenarios que lo requieren
    context["service"].create_expense(
        title="Gasto inicial",
        amount=amount,
        description="",
        expense_date=date.today(),
    )


@when(parsers.parse("añado un gasto de {amount:d} euros llamado {title}"))
def add_expense(context, amount, title):
    # Simula la acción del usuario añadiendo un gasto
    context["service"].create_expense(
        title=title,
        amount=amount,
        description="",
        expense_date=date.today(),
    )


@when(parsers.parse("elimino el gasto con id {expense_id:d}"))
def remove_expense(context, expense_id):
    # Simula la eliminación de un gasto
    context["service"].remove_expense(expense_id)


@then(parsers.parse("el total de dinero gastado debe ser {total:d} euros"))
def check_total(context, total):
    # Verifica la lógica de negocio del cálculo total
    assert context["service"].total_amount() == total


@then(parsers.parse("debe haber {expenses:d} gastos registrados"))
def check_expenses_length(context, expenses):
    # Verifica que el repositorio mantiene la cantidad correcta de gastos
    total = len(context["db"]._expenses)
    assert expenses == total