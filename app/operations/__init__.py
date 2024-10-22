from app.operations.abstract import TemplateOperation
from app.history.logging import logging


class Addition(TemplateOperation):
    """
    Class to represent the addition operation.
    Inherits from TemplateOperation.
    """
    def execute(self, a: float, b: float) -> float:
        """
        Returns the sum of two numbers.
        """
        return a + b  # Perform addition.

class Subtraction(TemplateOperation):
    """
    Class to represent the subtraction operation.
    Inherits from TemplateOperation.
    """
    def execute(self, a: float, b: float) -> float:
        """
        Returns the difference between two numbers.
        """
        return a - b  # Perform subtraction.

class Multiplication(TemplateOperation):
    """
    Class to represent the multiplication operation.
    Inherits from TemplateOperation.
    """
    def execute(self, a: float, b: float) -> float:
        """
        Returns the product of two numbers.
        """
        return a * b  # Perform multiplication.

class Division(TemplateOperation):
    """
    Class to represent the division operation.
    Inherits from TemplateOperation.
    """
    def execute(self, a: float, b: float) -> float:
        """
        Returns the quotient of two numbers.
        Raises a ValueError if attempting to divide by zero.
        """
        if b == 0:
            logging.error("Attempted to divide by zero.")  # Log an error message.
            raise ValueError("Division by zero is not allowed.")  # Raise an exception.
        return a / b  # Perform division.

# Why use the Template Method Pattern here?
# - It defines the algorithm's skeleton in a method (`calculate`), deferring some steps (`execute`) to subclasses.
# - Promotes code reuse and enforces a consistent structure across different operations.
