"""
Homework1 - Task 6 Tests
Robin Levisky
Handles files.
"""
import os
from ..src import task6

def test_words():
    """Tests words_in_task6 function by comparing to manual count."""
    file = open(os.path.dirname(__file__) + "/../task6_read_me.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()
    assert task6.words_in_task6() == len(content.split())
