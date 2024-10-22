from dataclasses import dataclass

from app.operations import TemplateOperation

# ==============================================================================
# STRATEGY PATTERN FOR OPERATION SELECTION
# ==============================================================================

# Who: The Calculation class.
# What: Represents a calculation using a specific strategy (operation).
# Why: To encapsulate algorithms (operations) and make them interchangeable.
# Where: In the execution of calculations.
# When: When performing operations on operands.
# How: By holding a reference to a strategy object and executing it.
@dataclass  # Decorator to automatically generate special methods like __init__.
class Calculation:
    """
    Represents a single calculation using the Strategy Pattern.
    Holds the operation (strategy) and operands.
    """
    operation: TemplateOperation  # The operation to execute (strategy).
    operand1: float  # The first operand.
    operand2: float  # The second operand.

    def __repr__(self) -> str:
        """
        Official string representation of the Calculation object.
        Used for debugging and logging.
        """
        return f"Calculation({self.operand1}, {self.operation.__class__.__name__.lower()}, {self.operand2})"

    def __str__(self) -> str:
        """
        User-friendly string representation of the calculation and result.
        """
        result = self.operation.calculate(self.operand1, self.operand2)  # Perform the calculation.
        return f"{self.operand1} {self.operation.__class__.__name__.lower()} {self.operand2} = {result}"

# Why use the Strategy Pattern?
# - Allows the algorithm (operation) to vary independently from the clients that use it.
# - Promotes flexibility and reuse of algorithms.
