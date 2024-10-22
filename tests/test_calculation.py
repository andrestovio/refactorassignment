"""
Unit tests for the Calculation class, using a MockOperation to simulate arithmetic operations.
"""
import unittest
from app.calculation import Calculation

class MockOperation:  # pylint: disable=too-few-public-methods
    """
    A mock operation class that simulates a basic arithmetic operation by 
    returning the sum of two operands.
    """

    def calculate(self, operand1, operand2):
        """Just return the sum of the two operands to simulate an addition operation."""
        return operand1 + operand2


class TestCalculation(unittest.TestCase):
    """
    Unit tests for the Calculation class to test its string representation and calculation.
    """

    def setUp(self):
        # Setup any common test data or operations here
        self.operation = MockOperation()  # Use the mock operation
        self.operand1 = 5.0
        self.operand2 = 3.0

    def test_calculation_repr(self):
        """
        Test the __repr__ method of the Calculation class.
        """
        calc = Calculation(self.operation, self.operand1, self.operand2)
        expected_repr = "Calculation(5.0, mockoperation, 3.0)"
        self.assertEqual(repr(calc), expected_repr)

    def test_calculation_str(self):
        """
        Test the __str__ method of the Calculation class.
        """
        calc = Calculation(self.operation, self.operand1, self.operand2)
        expected_str = "5.0 mockoperation 3.0 = 8.0"
        self.assertEqual(str(calc), expected_str)

    def test_calculate_result(self):
        """
        Test if the result of the calculation is correct.
        """
        result = self.operation.calculate(self.operand1, self.operand2)
        self.assertEqual(result, 8.0)

if __name__ == '__main__':
    unittest.main()
