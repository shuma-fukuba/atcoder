import pytest

from sorting.bubble_sort import bubble_sort
from sorting.insertion_sort import insertion_sort
from sorting.selection_sort import selection_sort
from sorting.quick_sort import quick_sort


def test_bubble_sort():
    nums = [2,3, 1, 5, 7,6]
    assert [1, 2, 3, 5, 6, 7] == bubble_sort(nums)


def test_selection_sort():
    nums = [2,3, 1, 5, 7,6]
    assert [1, 2, 3, 5, 6, 7] == selection_sort(nums)


def test_insertion_sort():
    nums = [2,3, 1, 5, 7,6]
    assert [1, 2, 3, 5, 6, 7] == insertion_sort(nums)

def test_quick_sort():
    nums = [2,3, 1, 5, 7,6]
    assert [1, 2, 3, 5, 6, 7] == quick_sort(nums)
