import pytest
import lec10
def test_linear_search():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(L, 5) is True
    assert lec10.linear_search(L, 18) is True
    assert lec10.linear_search(L, 2) is False
    assert lec10.linear_search([], 1) is False

def test_search_sorted():
    L = [1, 3, 5, 7, 9, 11]
    assert lec10.search(L, 3) is True     # in list
    assert lec10.search(L, 2) is False    # smaller and skipped
    assert lec10.search(L, 12) is False   # larger than max
    assert lec10.search([], 1) is False   # empty list

def test_is_subset():
    assert lec10.isSubset([1, 2], [1, 2, 3]) is True
    assert lec10.isSubset([1, 2, 4], [1, 2, 3]) is False
    assert lec10.isSubset([], [1, 2, 3]) is True
    assert lec10.isSubset([1], []) is False

def test_intersect():
    assert lec10.intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert lec10.intersect([1, 2], [3, 4]) == []
    assert lec10.intersect([], [1, 2]) == []
    assert lec10.intersect([1, 2, 2, 3], [2, 2, 3]) == [2, 3]

