import unittest
from numbers_of_upper_lower import print_letters

class PrintLetters(unittest.TestCase):


    def test_upper_lower(self):
        self.assertEqual(print_letters("Hello World"), (2, 8))

    def test_only_upper(self):
        self.assertEqual(print_letters("CAR"), (3, 0))

    def test_only_lower(self):
        self.assertEqual(print_letters("cowboy"), (0, 6))

    def test_empty_string(self):
        self.assertEqual(print_letters(""),(0,0))

if __name__=="__main__":
    unittest.main()
