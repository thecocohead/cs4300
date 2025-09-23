"""
Homework1 - Task 3
Robin Levisky
Tests control structures. 
"""
def is_positive(num: int) -> str:
    """Returns whether a number is positive, negative, or zero."""
    if num == 0:
        return "Zero"
    if num > 0:
        return "Positive"
    return "Negative"

def is_prime(num) -> bool:
    """Returns whether a number is prime."""
    divisor = 2
    num_sqrt = pow(num, 0.5)
    while divisor <= num_sqrt:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

def prime_numbers(count: int) -> list[int]:
    """Returns a list of the first 'count' prime numbers."""
    current_number = 2
    primes = []
    for i in range(count):
        prime_found = False
        while not prime_found:
            if is_prime(current_number):
                primes.append(current_number)
                prime_found = True
            current_number += 1
    return primes

def sum_numbers(min_num: int, max_num: int) -> int:
    """Returns the sum of all numbers between min and max, inclusive."""
    total = 0
    for i in range(min_num, max_num + 1):
        total += i
    return total
