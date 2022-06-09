import unittest


class TestStringMethods(unittest.TestCase):

    def test_string_length(self):
        assert(len(random_string_gen(5)), 5)


if __name__ == '__main__':
    unittest.main()
