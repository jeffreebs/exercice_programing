import unittest
from around_string import reversed_string

class TestReverseString(unittest.TestCase):
    

    def test_reverse(self):
        self.assertEqual(reversed_string(), "dneirf ym olleH")

    def test_reverse_empty_string(self):
        self.assertEqual(reversed_string(""), "")

    def test_reverse_mixt(self):
        self.assertEqual(reversed_string("ABC123xyz789"), "987zyx321CBA")

    


if __name__=="__main__":
    unittest.main()