"""
This module contains unit tests for the SingletonCalculator class and the MockOperation class,
which extends the TemplateOperation class. It includes tests for verifying that the singleton 
pattern is enforced and that the operations and shared history are working correctly.
"""
import pytest
from app.calculator.singleton import SingletonCalculator
from app.operations.abstract import TemplateOperation

# Mock Operation class that extends TemplateOperation
class MockOperation(TemplateOperation):
    """
    A mock operation class that simulates a simple addition operation for testing.
    It extends the TemplateOperation class and implements the execute method.
    """

    def execute(self, a: float, b: float) -> float:
        # Simple addition operation for testing
        return a + b

# Parametrized test for different operations
@pytest.mark.parametrize(
    "operation, a, b, expected_result", [
        (MockOperation(), 5, 3, 8.0),  # Test for addition (5 + 3)
        (MockOperation(), 10, 7, 17.0),  # Test for addition (10 + 7)
        (MockOperation(), 15, 5, 20.0),  # Test for addition (15 + 5)
    ]
)
def test_singleton_calculator_operations(operation, a, b, expected_result):
    """
    Parametrized test for performing different operations using SingletonCalculator.
    This test checks that the correct results are returned and that the shared history is updated.
    """
    calculator = SingletonCalculator()  # Create SingletonCalculator instance

    # Perform the operation and get the result
    result = calculator.perform_operation(operation, a, b)

    # Check if the result matches the expected result
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    # Check that the history contains the calculation
    history = calculator.get_history()
    assert len(history) > 0, "The history should contain at least one calculation."
    last_calculation = history[-1]  # Get the last calculation in history
    assert last_calculation.operand1 == a
    assert last_calculation.operand2 == b
    assert last_calculation.operation == operation

# Test that the singleton pattern is enforced
def test_singleton_instance():
    """
    Test that SingletonCalculator creates only one instance.
    """
    calculator1 = SingletonCalculator()
    calculator2 = SingletonCalculator()

    # Ensure both variables point to the same instance
    assert calculator1 is calculator2, "Singleton pattern is broken. Multiple instances exist."

    # Check that the history is shared
    calculator1.perform_operation(MockOperation(), 1, 2)
    assert len(calculator2.get_history()) == 4, "History is not shared between singleton instances."
