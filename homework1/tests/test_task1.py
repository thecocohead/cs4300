"""
Homework1 - Task 1 Tests
Robin Levisky
Prints "Hello, world!" to the console.
"""

from ..src import task1

def test_print_hello_world(capsys):
    """Tests that the function prints 'Hello, world!' to the console."""
    task1.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
