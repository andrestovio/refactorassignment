# Ultimate Guide to OOP Design Patterns: Building a Calculator with Logging and Debugging

# ==============================================================================
# IMPORTING NECESSARY MODULES
# ==============================================================================

import pdb  # Python debugger for interactive debugging sessions.
# Documentation: https://docs.python.org/3/library/pdb.html

from typing import List

from app.history.logging import logging
from app.calculator import CalculatorWithObserver
from app.history import HistoryObserver
from app.operations.factory import OperationFactory  # Provides support for type hints.
# Documentation: https://docs.python.org/3/library/typing.html

# ==============================================================================
# MAIN CALCULATOR PROGRAM (REPL INTERFACE WITH DEBUGGING)
# ==============================================================================

# Who: The calculator() function.
# What: Provides an interactive command-line interface for users to perform calculations.
# Why: To allow users to interact with the calculator in real-time.
# Where: In the main execution of the program.
# When: When the script is run directly.
# How: By implementing a Read-Eval-Print Loop (REPL).

def calculator():
    """
    Interactive REPL (Read-Eval-Print Loop) for performing calculator operations.
    Provides a command-line interface for users to interact with the calculator.
    """
    import pdb  # Import pdb module for debugging.

    # Create an instance of the calculator with observer support.
    calc = CalculatorWithObserver()

    # Create an observer to monitor calculation history.
    observer = HistoryObserver()

    # Add the observer to the calculator's list of observers.
    calc.add_observer(observer)

    # Display a welcome message and instructions.
    print("Welcome to the OOP Calculator! Type 'help' for available commands.")

    # Start the REPL loop.
    while True:
        # Prompt the user for input.
        user_input = input("Enter an operation and two numbers, or a command: ")

        # Handle the 'help' command.
        if user_input.lower() == "help":
            print("\nAvailable commands:")
            print("  add <num1> <num2>       : Add two numbers.")
            print("  subtract <num1> <num2>  : Subtract the second number from the first.")
            print("  multiply <num1> <num2>  : Multiply two numbers.")
            print("  divide <num1> <num2>    : Divide the first number by the second.")
            print("  list                    : Show the calculation history.")
            print("  clear                   : Clear the calculation history.")
            print("  exit                    : Exit the calculator.\n")
            continue  # Return to the start of the loop.

        # Handle the 'exit' command.
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break  # Exit the loop and end the program.

        # Handle the 'list' command to display calculation history.
        if user_input.lower() == "list":
            if not calc._history:
                print("No calculations in history.")
            else:
                for calc_item in calc._history:
                    print(calc_item)  # Calls __str__ method of Calculation.
            continue  # Return to the start of the loop.

        # Handle the 'clear' command to clear the history.
        if user_input.lower() == "clear":
            calc._history.clear()  # Clear the history list.
            logging.info("History cleared.")  # Log the action.
            print("History cleared.")
            continue  # Return to the start of the loop.

        # Attempt to parse and execute the user's command.
        try:
            # Set a breakpoint for debugging.
            # pdb.set_trace()  # Execution will pause here, allowing inspection of variables.

            # Split the user input into components.
            operation_str, num1_str, num2_str = user_input.split()  # May raise ValueError.

            # Convert the operand strings to float.
            num1, num2 = float(num1_str), float(num2_str)  # May raise ValueError.

            # Use the factory to create the appropriate operation object.
            operation = OperationFactory.create_operation(operation_str)

            if operation:
                # Perform the operation using the calculator.
                result = calc.perform_operation(operation, num1, num2)
                # Display the result to the user.
                print(f"Result: {result}")
            else:
                # Handle unknown operation names.
                print(f"Unknown operation '{operation_str}'. Type 'help' for available commands.")

        except ValueError as e:
            # Handle errors such as incorrect input format or invalid numbers.
            logging.error(f"Invalid input or error: {e}")  # Log the error.
            print("Invalid input. Please enter a valid operation and two numbers. Type 'help' for instructions.")

# Why use a REPL?
# - Provides an interactive way for users to execute commands and see immediate results.
# - Enhances user experience and allows for real-time feedback.

# ==============================================================================
# RUNNING THE CALCULATOR PROGRAM
# ==============================================================================

if __name__ == "__main__":
    # This block ensures that the calculator runs only when the script is executed directly.
    # It will not run if the script is imported as a module.
    calculator()  # Call the main calculator function to start the REPL.

# General Programming Good Practices Demonstrated:
# - **Modular Design**: The code is organized into classes and functions, making it easier to understand and maintain.
# - **Encapsulation**: Data and methods are encapsulated within classes, promoting data hiding and abstraction.
# - **Inheritance and Polymorphism**: Base classes define common interfaces, and derived classes implement specific behaviors.
# - **Exception Handling**: The code anticipates and handles potential errors gracefully, providing informative feedback.
# - **Logging**: Comprehensive logging is implemented to track the application's behavior and assist in debugging.
# - **Type Hinting**: Type hints improve code readability and help with static analysis tools.
# - **Documentation and Comments**: Detailed comments and docstrings explain the purpose and functionality of code components.
# - **Adherence to PEP 8**: The code follows Python's style guidelines for improved readability.

# Additional Resources and References:
# - **Abstract Base Classes (`abc` module)**:
#   - Reference: https://docs.python.org/3/library/abc.html
# - **Data Classes (`dataclasses` module)**:
#   - Reference: https://docs.python.org/3/library/dataclasses.html
# - **Type Hints (`typing` module)**:
#   - Reference: https://docs.python.org/3/library/typing.html
# - **Logging (`logging` module)**:
#   - Reference: https://docs.python.org/3/library/logging.html
# - **Python Debugger (`pdb` module)**:
#   - Reference: https://docs.python.org/3/library/pdb.html
# - **Design Patterns in Python**:
#   - Reference: https://refactoring.guru/design-patterns/python
# - **PEP 8 - Style Guide for Python Code**:
#   - Reference: https://www.python.org/dev/peps/pep-0008/

# Conclusion:
# This code serves as a comprehensive example of how to implement several key object-oriented design patterns in Python.
# By understanding the who, what, why, where, when, and how of each component, students can gain a deeper appreciation
# for the art and science of OOP. The combination of design patterns, logging, debugging, and good programming practices
# results in code that is robust, maintainable, and scalable.
