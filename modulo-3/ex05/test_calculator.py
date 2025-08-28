import pytest
import calculator


def test_add() -> None:
    """add"""
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0


def test_subtract() -> None:
    """subtract"""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 15) == -5


def test_multiply() -> None:
    """multi"""
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10


def test_divide() -> None:
    """divide"""
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(9, 4) == 2.25


def test_divide_by_zero() -> None:
    """check zero"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)

def test_power() -> None:
    """power"""
    assert calculator.power(2, 2) == 4
    assert calculator.power(2, 0) == 1
    assert calculator.power(-2, 2) == 4
    assert calculator.power(2, -3) == 0.125