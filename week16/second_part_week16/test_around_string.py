import unittest
from around_string import reversed_string

class TestReverseString(unittest.TestCase):
    

    def test_reverse(self):
        self.assertEqual(reversed_string(), "dneirf ym olleH")


if __name__=="__main__":
    unittest.main()