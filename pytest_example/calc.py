class CalculatorError(Exception):
    """And exception class for calculator"""


class Calculator:

    @staticmethod
    def add(x, y):
        """Add Function"""
        return x + y

    @staticmethod
    def subtract(x, y):
        """Subtract Function"""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Multiply Function"""
        return x * y

    @staticmethod
    def divide(x, y):
        """Divide Function"""
        if y == 0:
            raise CalculatorError('Can not divide by zero!')
        return x / y
