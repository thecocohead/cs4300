"""
Homework1 - Task 3 Tests
Robin Levisky
Tests control structures. 
"""

from ..src import task3


def test_is_positive():
    """Tests is_positive function."""
    assert task3.is_positive(10) == "Positive"
    assert task3.is_positive(-5) == "Negative"
    assert task3.is_positive(0) == "Zero"

def test_is_prime():
    """Tests is_prime function."""
    assert task3.is_prime(2) is True
    assert task3.is_prime(3) is True
    assert task3.is_prime(4) is False
    assert task3.is_prime(17) is True
    assert task3.is_prime(18) is False

def test_prime_numbers():
    """Tests prime_numbers function."""
    print(task3.prime_numbers(10))
    assert task3.prime_numbers(5) == [2, 3, 5, 7, 11]
    assert task3.prime_numbers(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task3.prime_numbers(0) == []
    assert task3.prime_numbers(1) == [2]

def test_sum_numbers():
    """Tests sum_numbers function."""
    assert task3.sum_numbers(1, 5) == 15
    assert task3.sum_numbers(-3, 3) == 0
    assert task3.sum_numbers(0, 0) == 0
    assert task3.sum_numbers(10, 20) == 165

    # Actual Homework assignment
    assert task3.sum_numbers(1, 100) == 5050
