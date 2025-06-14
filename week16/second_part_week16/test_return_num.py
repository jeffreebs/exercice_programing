import unittest
from return_num import return_the_sum_of_list

class TestReturnNum(unittest.TestCase):


    def test_return_sum_of_list(self):
        self.assertEqual(return_the_sum_of_list(),150)
        self.assertEqual(return_the_sum_of_list([1, 2, 3]), 6)
        self.assertEqual(return_the_sum_of_list([]), 0)
        self.assertEqual(return_the_sum_of_list([-10,10]), 0)



if __name__ == "__main__":
    unittest.main()
        
