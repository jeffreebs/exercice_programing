import unittest

from order_string import order_strings

class TestOrder(unittest.TestCase):

    def test_order(self):
        self.assertEqual(order_strings("banana-apple-orange"), "apple-banana-orange")


    def test_ordered(self):
        self.assertEqual(order_strings("banana-apple-orange"), "apple-banana-orange")


    def test_reverse_order(self):
        self.assertEqual(order_strings("orange-banana-apple"), "apple-banana-orange")


    def test_order_single(self):
        self.assertEqual(order_strings("hello"), "hello")


if __name__=="__main__":
    unittest.main()