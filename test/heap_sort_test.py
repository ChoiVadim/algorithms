import unittest
from src.sort import heap_sort

class TestHeapSort(unittest.TestCase):
    test_cases = (
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
        ([1, 2, 3, -4, 5], [-4, 1, 2, 3, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    )

    def test_heap_sort(self):
        for inp, exp in self.test_cases:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(heap_sort(inp), exp)

if __name__ == '__main__':
    unittest.main()