# ==============================================================================
# OPERATION CLASSES (COMMAND AND TEMPLATE METHOD PATTERNS)
# ==============================================================================

# Who: These classes are the core components that perform arithmetic operations.
# What: Implement arithmetic operations using design patterns.
# Why: To demonstrate OOP principles and design patterns for clean, maintainable code.
# Where: In the calculator application we are building.
# When: Whenever an arithmetic operation is requested.
# How: By defining a base class and extending it for specific operations.

# We will implement the Command Pattern, where each operation (e.g., addition, subtraction)
# is encapsulated as an object. The Template Method Pattern is used to define the
# skeleton of an algorithm, deferring some steps to subclasses.

from abc import ABC, abstractmethod

from app.history.logging import logging 


class TemplateOperation(ABC):
    """
    Abstract base class representing a mathematical operation using the Template Method pattern.
    - Inherits from ABC to make it an abstract base class.
    - The Template Method Pattern defines the steps of an algorithm.
    """
    def calculate(self, a: float, b: float) -> float:
        """
        Template method that defines the structure for performing an operation.
        Steps:
        1. Validate inputs.
        2. Execute the operation.
        3. Log the result.
        """
        self.validate_inputs(a, b)  # Step 1: Validate the inputs.
        result = self.execute(a, b)  # Step 2: Perform the specific operation.
        self.log_result(a, b, result)  # Step 3: Log the operation and the result.
        return result  # Return the result of the operation.

    def validate_inputs(self, a: float, b: float):
        """
        Common validation method to ensure inputs are numbers.
        Raises a ValueError if inputs are not numeric types.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logging.error(f"Invalid input: {a}, {b} (Inputs must be numbers)")  # Log an error message.
            raise ValueError("Both inputs must be numbers.")  # Raise an exception.

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """
        Abstract method to perform the specific operation.
        Must be implemented by subclasses.
        """
        pass  # pragma: no cover 

    def log_result(self, a: float, b: float, result: float):
        """
        Logs the result of the calculation.
        """
        logging.info(f"Operation performed: {a} and {b} -> Result: {result}")  # Log an informational message.


# Concrete operation classes implementing specific arithmetic operations.
# Each class represents a specific operation and extends the TemplateOperation base class.