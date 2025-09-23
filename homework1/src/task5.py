"""
Homework1 - Task 5
Robin Levisky
Tests usages of lists and dictionaries. 
"""

def books():
    """Prints a list of books."""
    book_list = [
        "aaa by 111",
        "bbb by 222",
        "ccc by 333",
        "ddd by 444",
    ]
    print(book_list[0:3])

def students():
    """Returns a dictionary of students and their IDs."""
    student_dict = {
        "AAA": 129571294,
        "BBB": 124912748,
        "CCC": 124957175,
        "DDD": 125017274,
    }
    return student_dict
