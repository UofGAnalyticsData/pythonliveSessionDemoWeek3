from helpfulfuncs import math_funcs
import pytest

def test_factorial_5():
    test_value = 5
    expected_result = 120
    result = math_funcs.factorial(test_value)
    assert result == expected_result

def test_factorial_0():
    test_value = 0
    expected_result = 1
    result = math_funcs.factorial(test_value)
    assert result == expected_result

def test_factorial_negative():
    test_value = -5
    with pytest.raises(ValueError):
        math_funcs.factorial(test_value)

def test_factorial_non_integer():
    test_value = 5.5
    with pytest.raises(ValueError):
        math_funcs.factorial(test_value)


def test_factorial_list():
    test_value = [1,2,3] 
    with pytest.raises(ValueError):
        math_funcs.factorial(test_value)

