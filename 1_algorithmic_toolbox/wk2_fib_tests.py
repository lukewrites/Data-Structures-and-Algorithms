"""Tests for wk2_fib.py."""

from .wk2_fib import calc_fib
import unittest


class testCalcFib(unittest.TestCase):
    """Tests for the calc_fib(n) function."""

    def setUp(self):
        self.fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

    def test_if_0_calculates_correctly(self):
        self.assertEqual(calc_fib(0), 0)

    def test_if_1_calculates_correctly(self):
        self.assertEqual(calc_fib(1), 1)

    def test_if_9_calculates_correctly(self):
        self.assertEqual(calc_fib(9), self.fib_numbers[9])

    def test_if_7_calculates_correctly(self):
        self.assertEqual(calc_fib(7), self.fib_numbers[7])

if __name__ == '__main__':
    unittest.main()
