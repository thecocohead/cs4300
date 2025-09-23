"""
Homework1 - Task 4 Tests
Robin Levisky
Calculate the discounted price of an item given its original price and a discount percentage.
"""

from ..src import task4


def test_calculate_discount():
    """Tests calculate_discount function."""
    assert task4.calculate_discount(100, 10) == 90.0
    assert task4.calculate_discount(0, 10) == 0.0
    assert task4.calculate_discount(100, 0) == 100.0
    assert task4.calculate_discount(100, 200) == -100.0
    assert task4.calculate_discount(50.5, 10) == 45.45
    assert task4.calculate_discount(100, 33.33) == 66.67
    assert task4.calculate_discount(int(100), int(10)) == 90.0
