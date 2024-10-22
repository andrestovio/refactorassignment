# ==============================================================================
# FACTORY PATTERN FOR CREATING OPERATIONS
# ==============================================================================

# Who: The OperationFactory class.
# What: Creates instances of operation classes based on a given operation name.
# Why: To encapsulate object creation, promoting loose coupling and adherence to the Open/Closed Principle.
# Where: Used whenever a new operation needs to be created based on user input.
# When: At runtime, during the calculator's execution.
# How: By mapping operation names to their corresponding classes.

from app.operations.abstract import TemplateOperation
from app.history.logging import logging
from app.operations import Addition, Division, Multiplication, Subtraction


class OperationFactory:
    """
    Factory class to create instances of operations based on the operation type.
    Implements the Factory Pattern.
    """
    @staticmethod
    def create_operation(operation: str) -> TemplateOperation:
        """
        Returns an instance of the appropriate Operation subclass based on the operation string.
        Parameters:
        - operation (str): The operation name (e.g., 'add', 'subtract').
        """
        # Dictionary mapping operation names to their corresponding class instances.
        operations_map = {
            "add": Addition(),
            "subtract": Subtraction(),
            "multiply": Multiplication(),
            "divide": Division(),
        }
        # Log the operation creation request at DEBUG level.
        logging.debug(f"Creating operation for: {operation}")
        # Retrieve the operation instance from the map.
        return operations_map.get(operation.lower())  # Returns None if the key is not found.
    
    # Why use the Factory Pattern?
# - It provides a way to create objects without specifying the exact class.
# - Enhances flexibility and scalability; new operations can be added without modifying existing code.
