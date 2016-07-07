import unittest
from wk1_maximum_pairwise_product import mpp


class testMPP(unittest.TestCase):

    def setUp(self):
        self.even_list = [5, 1, 3, 2, 4]
        self.weird_list = [5, 1, 3, 2, 4, 9]
        self.odd_list = [5, 4, 3]
        self.empty_list = []

    def test_if_an_even_list_works(self):
        self.assertEqual(mpp(self.even_list), 20)

    def test_if_an_odd_list_works(self):
        """Does it work if there are an odd number of items in the list?"""
        self.assertEqual(mpp(self.odd_list), 20)

    def test_if_an_empty_list_works(self):
        self.assertFalse(mpp(self.empty_list))  # just for fun.
        self.assertEqual(mpp(self.empty_list), 0)

    def test_weird_list(self):
        self.assertEqual(mpp(self.weird_list), 45)


if __name__ == '__main__':
    unittest.main()
