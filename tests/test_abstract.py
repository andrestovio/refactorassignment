"""
Unit tests for arithmetic operations using pytest, including input validation and logging checks.
"""
import pytest
from app.operations.abstract import TemplateOperation
from app.operations.factory import Addition, Subtraction, Multiplication, Division
from app.history import logging  # Import the logging configuration from your logging file

class CustomOperation(TemplateOperation):
    """A custom subclass of TemplateOperation to test the validate_inputs method."""
    def execute(self, a: float, b: float) -> float:

        return a + b  # A dummy implementation for testing validate_inputs


def test_validate_inputs_success(caplog):
    """
    Test that validate_inputs succeeds with valid numeric inputs.
    """
    operation = CustomOperation()

    # No exception should be raised here, and no logs for invalid input.
    with caplog.at_level(logging.DEBUG):  # Ensure log capture
        operation.validate_inputs(5, 10)  # Valid inputs: no exception

    # Assert that no logging errors were triggered
    assert "Invalid input" not in caplog.text


def test_validate_inputs_failure_non_numeric(caplog):
    """
    Test that validate_inputs raises a ValueError for non-numeric inputs.
    """
    operation = CustomOperation()

    with caplog.at_level(logging.DEBUG):
        with pytest.raises(ValueError, match="Both inputs must be numbers."):
            operation.validate_inputs(5, "invalid")  # Invalid input: second value is a string

        # Assert that an appropriate error log was created
        assert "Invalid input: 5, invalid (Inputs must be numbers)" in caplog.text


def test_validate_inputs_failure_both_non_numeric(caplog):
    """
    Test that validate_inputs raises a ValueError when both inputs are non-numeric.
    """
    operation = CustomOperation()

    with caplog.at_level(logging.DEBUG):
        with pytest.raises(ValueError, match="Both inputs must be numbers."):
            operation.validate_inputs("invalid1", "invalid2")  # Both inputs invalid

        # Assert that an appropriate error log was created
        assert "Invalid input: invalid1, invalid2 (Inputs must be numbers)" in caplog.text


# Parametrized test for the concrete operation classes
@pytest.mark.parametrize(
    "operation_class, a, b, expected_result", [
        (Addition(), 5, 3, 8),          # Test addition
        (Subtraction(), 10, 4, 6),      # Test subtraction
        (Multiplication(), 7, 3, 21),   # Test multiplication
        (Division(), 20, 5, 4),         # Test division
        (Division(), 5, 0, ValueError), # Test division by zero
    ]
)
def test_operations(operation_class, a, b, expected_result, caplog):
    """
    Parametrized test to simulate different arithmetic operations.
    Captures the log output to ensure logging functionality is working as expected.
    """
    with caplog.at_level(logging.DEBUG):  # Ensure we capture DEBUG level logs
        try:
            result = operation_class.calculate(a, b)
            assert result == expected_result, f"Expected {expected_result}, but got {result}"

            # Verify logging for valid operations
            assert "Operation performed" in caplog.text, f"Log output: {caplog.text}"

        except ValueError as e:
            # Handle division by zero or any other ValueErrors
            if isinstance(operation_class, Division) and b == 0:
                assert "Attempted to divide by zero" in caplog.text, f"Log output: {caplog.text}"
            else:
                raise e
