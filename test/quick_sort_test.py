import unittest
from sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_quick_sort_single_element_list(self):
        self.assertEqual(quick_sort([1]), [1])

    def test_quick_sort_two_elements_list(self):
        self.assertEqual(quick_sort([2, 1]), [1, 2])

    def test_quick_sort_three_elements_list(self):
        self.assertEqual(quick_sort([3, 2, 1]), [1, 2, 3])

    def test_quick_sort_reverse_order_list(self):
        self.assertEqual(quick_sort([1, 2, 3]), [1, 2, 3])

    def test_quick_sort_random_list(self):
        self.assertEqual(
            quick_sort([5, 3, 8, 1, 6, 2, 9, 4, 7]), [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )


if __name__ == "__main__":
    unittest.main()
