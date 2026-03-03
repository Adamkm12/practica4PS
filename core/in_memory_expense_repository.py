from core.expense import Expense
from core.expense_service import ExpenseRepository


class InMemoryExpenseRepository(ExpenseRepository):
    def __init__(self):
        self._expenses: list[Expense] = []

    def save(self, expense: Expense) -> None:
        for index, existing in enumerate(self._expenses):
            if existing.id == expense.id:
                self._expenses[index] = expense
                return
        self._expenses.append(expense)

    def remove(self, expense_id: int) -> None:
        # Corrección: se recorre la lista y se elimina el gasto con la id indicada
        # Usamos enumerate para poder eliminar por índice de forma segura
        for index, expense in enumerate(self._expenses):
            if expense.id == expense_id:
                del self._expenses[index]
                return

    def get_by_id(self, expense_id: int) -> Expense | None:
        return next(
            (expense for expense in self._expenses if expense.id == expense_id), None
        )

    def list_all(self) -> list[Expense]:
        return list(self._expenses)
