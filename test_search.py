from src.sort import quick_sort


def test_quick_sort1():
    assert quick_sort([]) == []


def test_quick_sort2():
    assert quick_sort([1]) == [1]


def test_quick_sort3():
    assert quick_sort([1, 2, 3]) == [1, 2, 3]


def test_quick_sort4():
    assert quick_sort([3, 2, 1, 5, 4]) == [1, 2, 3, 4, 5]


def test_quick_sort5():
    assert quick_sort([5, 3, 8, 1, 6, 2, 9, 4, 7]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
