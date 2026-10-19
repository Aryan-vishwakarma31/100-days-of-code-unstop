import pytest
from Day_01_exchanging import find_judge


def test_find_judge_basic():
    # Example: person 2 is judge
    assert find_judge(3, [(1,2),(3,2)]) == 2

def test_find_judge_none():
    assert find_judge(3, [(1,2),(2,3)]) == -1
