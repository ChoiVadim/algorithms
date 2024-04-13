import unittest
from src.sort import merge_sort
class TestMergeSort(unittest.TestCase):

    def test_merge_sort_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_merge_sort_single_element_list(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_merge_sort_list_of_two_elements(self):
        self.assertEqual(merge_sort([2, 1]), [1, 2])

    def test_merge_sort_list_of_three_elements(self):
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])

    def test_merge_sort_list_of_four_elements(self):
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_merge_sort_list_of_five_elements(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_merge_sort_list_of_negative_elements(self):
        self.assertEqual(merge_sort([-5, -4, -3, -2, -1]), [-5, -4, -3, -2, -1])

    def test_merge_sort_list_of_mixed_elements(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1, -5, -4, -3, -2, -1]), [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()