"""
Homework1 - Task 2 Tests
Robin Levisky
Returns various data types.
"""
from ..src import task2


def test_return_int():
    """Tests return_int function."""
    assert task2.return_int() == 5

def test_return_str():
    """Tests return_str function."""
    assert task2.return_str() == "Hello"

def test_return_list():
    """Tests return_list function."""
    assert task2.return_list() == [1, 2, 3]

def test_return_bool():
    """Tests return_bool function."""
    assert task2.return_bool() is True

def test_return_float():
    """Tests return_float function."""
    assert task2.return_float() == 3.14
