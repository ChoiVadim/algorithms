import unittest
from math import sqrt


def fib_const_time(n):
    return round(
        1 / sqrt(5) * ((1 + sqrt(5)) / 2) ** n - 1 / sqrt(5) * ((1 - sqrt(5)) / 2) ** n
    )


class TestFibonacci(unittest.TestCase):
    def test_fib_const_time(self):
        for n, expected in [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (10, 55),
            (20, 6765),
            (30, 832040),
            (40, 102334155),
        ]:
            with self.subTest(n=n, expected=expected):
                self.assertAlmostEqual(fib_const_time(n), expected)


if __name__ == "__main__":
    unittest.main()
