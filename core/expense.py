from dataclasses import dataclass
from datetime import date

from core.domain_error import (
    InvalidAmountError,
    InvalidExpenseDateError,
    EmptyTitleError,
    idError,
)


@dataclass
class Expense:
    id: int
    title: str
    amount: float
    description: str
    expense_date: date

    def __post_init__(self):
        # Validar título
        if not self.title or self.title.strip() == "":
            raise EmptyTitleError("El título no puede estar vacío")

        # Validar importe
        if self.amount <= 0:
            raise InvalidAmountError("El importe debe ser mayor que 0")

        # Validar fecha (no futura)
        if self.expense_date > date.today():
            raise InvalidExpenseDateError(
                "La fecha del gasto no puede ser posterior a hoy"
            )
        
        if self.id < 0:
            raise idError("El id debe ser mayor a 0")
        
