"""Tests for wk1 mpp function."""


import unittest
from .wk1_maximum_pairwise_product import mpp  # this weird dot is here
                                               # because travis runs unittest
                                               # from the base directory.


class testMPP(unittest.TestCase):
    """Our testcases."""

    def setUp(self):
        """To be used across test cases."""
        self.even_list = [5, 1, 3, 2, 4]
        self.weird_list = [5, 1, 3, 2, 4, 9]
        self.odd_list = [5, 4, 3]
        self.empty_list = []
        self.evil_list = [9, 0, 0, 10]

    def test_if_an_even_list_works(self):
        """Check list with even number of items."""
        self.assertEqual(mpp(self.even_list), 20)

    def test_an_odd_list_works(self):
        """Check list with odd number of items."""
        self.assertEqual(mpp(self.odd_list), 20)

    def test_if_an_empty_list_works(self):
        """Check empty list."""
        self.assertFalse(mpp(self.empty_list))  # just for fun.
        self.assertEqual(mpp(self.empty_list), 0)

    def test_weird_list(self):
        """Check what happens when last number is largest."""
        self.assertEqual(mpp(self.weird_list), 45)

    def test_evil_list(self):
        """Test an evil list."""
        self.assertEqual(mpp(self.evil_list), 90)


if __name__ == '__main__':
    unittest.main()
