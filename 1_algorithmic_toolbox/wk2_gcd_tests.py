from .wk2_gcd import gcd
import unittest


class gcdTests(unittest.TestCase):
    """Tests for the gcd function."""

    def test_zeros(self):
        """Test if the gcd of two zeros is zero."""
        self.assertEqual(gcd(0, 0), 0)

    def test_zero_and_big(self):
        """Test if a zero and a huge number return the huge number."""
        self.assertEqual(gcd(1000000000, 0), 1000000000)

    def test_ten_and_two(self):
        """Test if the gcd of 10 and 2 is 2."""
        self.assertEqual(gcd(10, 2), 2)

    def test_two_that_do_not_share_gcd(self):
        """Test the gcd of two primes."""
        self.assertEqual(gcd(3, 5), 1)

if __name__ == '__main__':
    unittest.main()
