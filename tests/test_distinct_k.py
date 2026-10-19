import pytest
from Day_01_distinct import kth_distinct


def test_kth_distinct_found():
    assert kth_distinct(['a', 'b', 'a', 'c'], 2) == 'b'
    assert kth_distinct(['x', 'y', 'z'], 1) == 'x'


def test_kth_distinct_not_found():
    assert kth_distinct(['a', 'a'], 2) == '-1'
    assert kth_distinct([], 1) == '-1'
