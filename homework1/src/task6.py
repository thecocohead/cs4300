"""
Homework1 - Task 6
Robin Levisky
Handles files.
"""

import os

def words_in_task6() -> int:
    """Returns the number of words in task6_read_me.txt"""
    file = open(os.path.dirname(__file__) + "/../task6_read_me.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()
    num_words = len(content.split())
    return num_words
