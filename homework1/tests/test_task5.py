"""
Homework1 - Task 5 Tests
Robin Levisky
Tests usages of lists and dictionaries. 
"""

from ..src import task5


def test_books(capsys):
    """Tests lists output."""
    task5.books()
    captured = capsys.readouterr()
    assert captured.out == "['aaa by 111', 'bbb by 222', 'ccc by 333']\n"

def test_students():
    """Tests dictionaries output."""
    expected_students = {
        "AAA": 129571294,
        "BBB": 124912748,
        "CCC": 124957175,
        "DDD": 125017274,
    }
    assert task5.students() == expected_students
