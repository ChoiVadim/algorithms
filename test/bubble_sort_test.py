import unittest
from src.sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_bubble_sort_single_element_list(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_bubble_sort_ascending_list(self):
        self.assertEqual(bubble_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_bubble_sort_already_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_bubble_sort_duplicate_list(self):
        self.assertEqual(bubble_sort([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

    def test_bubble_sort_descending_list(self):
        self.assertEqual(bubble_sort([3, 2, 3, 2, 1], True), [3, 3, 2, 2, 1])

if __name__ == '__main__':
    unittest.main()