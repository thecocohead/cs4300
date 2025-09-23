"""
Homework1 - Task 7 Tests
Robin Levisky
Tests numpy
"""
import numpy as np

from ..src import task7

def test_dot_product():
    """Tests dot_product function by comparing to manual calculation."""
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert task7.dot_product(a, b) == 32

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[19, 22], [43, 50]])
    assert np.array_equal(task7.dot_product(a, b), expected_result)

    a = np.array([1])
    b = np.array([2])
    assert task7.dot_product(a, b) == 2

    a = np.array([])
    b = np.array([])
    assert task7.dot_product(a, b) == 0
