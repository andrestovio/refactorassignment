# ==============================================================================
# SINGLETON PATTERN FOR ENSURING ONE CALCULATOR INSTANCE
# ==============================================================================

# Who: The SingletonCalculator class.
# What: Ensures only one instance of the calculator exists.
# Why: To have a single shared state (e.g., calculation history) across the application.
# Where: In scenarios where shared resources are needed.
# When: Throughout the application's lifecycle.
# How: By controlling instance creation using the __new__ method.

from app.calculation import Calculation
from app.history.logging import logging
from app.operations.abstract import TemplateOperation


class SingletonCalculator:
    """
    A calculator using the Singleton pattern to ensure only one instance exists.
    """
    _instance = None  # Class variable to hold the singleton instance.

    def __new__(cls):
        """
        Overrides the __new__ method to control the creation of a new instance.
        Ensures that only one instance is created.
        """
        if cls._instance is None:
            cls._instance = super(SingletonCalculator, cls).__new__(cls)  # Call the superclass __new__ method.
            cls._history = []  # Initialize the shared history.
            logging.info("SingletonCalculator instance created.")  # Log the creation.
        return cls._instance  # Return the singleton instance.

    def perform_operation(self, operation: TemplateOperation, a: float, b: float) -> float:
        """
        Performs the given operation and stores the calculation in history.
        Parameters:
        - operation (TemplateOperation): The operation to perform.
        - a (float): The first operand.
        - b (float): The second operand.
        Returns:
        - The result of the operation.
        """
        calculation = Calculation(operation, a, b)  # Create a new Calculation object.
        self._history.append(calculation)  # Add the calculation to the shared history.
        logging.debug(f"SingletonCalculator: Performed operation -> {calculation}")  # Log the operation.
        return operation.calculate(a, b)  # Execute the calculation and return the result.

    def get_history(self):
        """
        Returns the history of calculations.
        Includes a breakpoint for debugging using pdb.
        """
       # pdb.set_trace()  # Pause execution here for debugging.
        return self._history  # Return the shared history list.

# Why use the Singleton Pattern?
# - To control access to a shared resource.
# - Ensures that there's only one point of interaction with the resource.
