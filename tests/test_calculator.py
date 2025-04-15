from calculator import add, subtract, multiply, divide, power
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
def test_divide():
    assert divide(6, 3) == 2
    assert divide(0, 1) == 0
def test_divide_by_zerp():
    with pytest.raises(ValueError):
        divide(1, 0)
def test_power():
    assert power(2, 3) == 8
    assert power(3, 0) == 1
    assert power(0, 3) == 0
