"""
This module contains unit tests for the OOP Calculator REPL function, using
parametrized test cases to validate different calculator operations and commands.
"""
from unittest import mock
import pytest
from app.main import calculator  # Import the REPL function from main.py



def normalize_output(output):
    """Replace multiple newlines and spaces with a single space and ensure "Exiting calculator..."""
    normalized = " ".join(output.split()).replace("Exiting calculator ...", "Exiting calculator...")
    return normalized

# Parametrized test for different calculator operations
@pytest.mark.parametrize(
    "user_input, expected_output", [
("add 5 3",
         "Welcome to the OOP Calculator! Type 'help' for available commands."
         "Result: 8.0Exiting calculator..."),

("subtract 10 4",
         "Welcome to the OOP Calculator! Type 'help' for available commands."
         "Result: 6.0Exiting calculator..."),

("multiply 7 3",
         "Welcome to the OOP Calculator! Type 'help' for available commands."
         "Result: 21.0Exiting calculator..."),

("divide 20 5",
         "Welcome to the OOP Calculator! Type 'help' for available commands."
         "Result: 4.0Exiting calculator..."),

("divide 5 0",
         "Welcome to the OOP Calculator! Type 'help' for available commands."
         "Invalid input. Please enter a valid operation and two numbers. "
         "Type 'help' for instructions.Exiting calculator..."),

("invalid 10 2",
         "Welcome to the OOP Calculator! Type 'help' for available commands."
         "Unknown operation 'invalid'. Type 'help' for available commands."
         "Exiting calculator..."),

("help",
         "Welcome to the OOP Calculator! Type 'help' for available commands. "
         "Available commands: add <num1> <num2> : Add two numbers. subtract "
         "<num1> <num2> : Subtract the second number from the first. multiply "
         "<num1> <num2> : Multiply two numbers. divide <num1> <num2> : Divide "
         "the first number by the second. list : Show the calculation history. "
         "clear : Clear the calculation history. exit : Exit the calculator. "
         "Exiting calculator..."),
    ]
)
def test_calculator_operations(user_input, expected_output):
    """
    Parametrized test to simulate different calculator operations and commands,
    ensuring the full output (including the welcome message and exit message) matches.
    """
    # Mock input to return the user_input value followed by "exit" to terminate the REPL
    with mock.patch('builtins.input', side_effect=[user_input, "exit"]):
        # Mock the print function to capture output
        with mock.patch('builtins.print') as mocked_print:
            calculator()  # Run the REPL

            # Combine all print calls into one string
            actual_output = ''.join([call.args[0] for call in mocked_print.call_args_list])

            # Print for debugging purposes
            print(f"Actual Output: {repr(actual_output)}")
            print(f"Expected Output: {repr(expected_output)}")

            # Normalize both actual and expected output
            normalized_actual_output = normalize_output(actual_output)
            normalized_expected_output = normalize_output(expected_output)

            # Strip any extra whitespace and compare
            assert normalized_actual_output == normalized_expected_output
