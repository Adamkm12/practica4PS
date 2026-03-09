class DomainError(Exception):
    """Error base del dominio"""

    pass

class idError(DomainError):
    pass

class EmptyTitleError(DomainError):
    pass


class InvalidAmountError(DomainError):
    pass


class InvalidExpenseDateError(DomainError):
    pass
