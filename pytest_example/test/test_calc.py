import pytest
from pytest_example import calc


def test_add():
    # Arrange
    calculator = calc.Calculator()

    # Act
    result = calculator.add(10, 5)

    # Assert
    assert result == 15


def test_subtract():
    # Arrange
    calculator = calc.Calculator()

    # Act
    result = calculator.subtract(10, 5)

    # Assert
    assert result == 5


def test_multiply():
    # Arrange
    calculator = calc.Calculator()

    # Act
    result = calculator.multiply(10, 5)

    # Assert
    assert result == 50


def test_divide():
    # Arrange
    calculator = calc.Calculator()

    # Act
    result = calculator.divide(10, 5)

    # Assert
    assert result == 2


def test_divide_by_zero():
    # Arrange
    calculator = calc.Calculator()

    # Act
    with pytest.raises(calc.CalculatorError)as context:
        result = calculator.divide(10, 0)

    # Assert
    assert str(context.value) == 'Can not divide by zero!'
