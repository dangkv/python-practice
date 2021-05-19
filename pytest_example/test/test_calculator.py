import pytest
from pytest_example import calculator_example as calc


@pytest.fixture
def calculator():
    return calc.Calculator()


@pytest.mark.operations
def test_add(calculator):
    """
    Test to see if add function works as expected
    """
    # Arrange

    # Act
    result = calculator.add(10, 5)

    # Assert
    assert result == 15

    # Cleanup


@pytest.mark.operations
def test_subtract(calculator):
    """
    Test to see if subtract function works as expected
    """
    # Arrange

    # Act
    result = calculator.subtract(10, 5)

    # Assert
    assert result == 5

    # Cleanup


@pytest.mark.operations
def test_multiply(calculator):
    """
    Test to see if multiply function works as expected
    """
    # Arrange

    # Act
    result = calculator.multiply(10, 5)

    # Assert
    assert result == 50

    # Cleanup


@pytest.mark.operations
def test_divide(calculator):
    """
    Test to see if divide function works as expected
    """
    # Arrange

    # Act
    result = calculator.divide(10, 5)

    # Assert
    assert result == 2

    # Cleanup


@pytest.mark.exceptions
def test_divide_by_zero(calculator):
    """
    Test to see if Raise Exception works as expected
    """
    # Arrange

    # Act
    with pytest.raises(calc.CalculatorError)as context:
        result = calculator.divide(10, 0)

    # Assert
    assert str(context.value) == 'Can not divide by zero!'

    # Cleanup
