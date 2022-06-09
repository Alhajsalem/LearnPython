import unittest
from madlibs import random_string_gen


class Test_random_string_gen(unittest.TestCase):
    def test1(self):
        actual = len(random_string_gen(5))
        expected = 5
        self.assertEqual(actual, expected)

    def test2(self):
        actual = len(random_string_gen(20))
        expected = 5
        self.assertNotEqual(actual, expected)
