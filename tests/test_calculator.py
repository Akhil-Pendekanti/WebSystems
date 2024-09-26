import pytest
from calculator import _init_

def test_add():
    assert calculator.add(1, 2) == 3

def test_subtract():
    assert Calculator.subtract(4, 2) == 2

def test_multiply():
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)
