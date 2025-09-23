"""
Homework1 - Task 4
Robin Levisky
Calculate the discounted price of an item given its original price and a discount percentage.
"""

def calculate_discount(price, discount):
    """Calculate the discounted price of an item."""
    return price - (price * discount / 100)
