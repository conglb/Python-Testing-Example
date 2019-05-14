import unittest
from src.function import gcd

class GcdTestCase(unittest.TestCase):
    def test_two_positive_integer(self):
        self.assertEqual(2, gcd(4, 18))
        self.assertEqual(3, gcd(21, 9))
        self.assertEqual(3, gcd(3, 300))

    def test_two_negative_integer(self):˚
        self.assertEqual(2, gcd(-18, -4))
        self.assertEqual(3, gcd(-9, -21))

    def test_two_different_sign_integer(self):
        self.assertEqual(2, gcd(2, -4))
        self.assertEqual(3, gcd(-300, 3))

    def test_exception(self):
        self.assertRaises(TypeError, gcd, 'hi', 2)
        self.assertRaises(TypeError, gcd, 'abc', 3)
        self.assertRaises(TypeError, gcd, 'hi', 'hello')
˚

