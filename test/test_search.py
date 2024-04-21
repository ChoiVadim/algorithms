import unittest
from search import ternary_search

class TestTernarySearch(unittest.TestCase):
    def test_target_at_first_mid_point(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 3
        self.assertEqual(ternary_search(array, 0, len(array) - 1, target), 2)

    def test_target_at_second_mid_point(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 7
        self.assertEqual(ternary_search(array, 0, len(array) - 1, target), 6)

    def test_target_in_left_segment(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 2
        self.assertEqual(ternary_search(array, 0, len(array) - 1, target), 1)

    def test_target_in_right_segment(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 8
        self.assertEqual(ternary_search(array, 0, len(array) - 1, target), 7)

    def test_target_not_found(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 11
        self.assertEqual(ternary_search(array, 0, len(array) - 1, target), -1)

if __name__ == '__main__':
    unittest.main()