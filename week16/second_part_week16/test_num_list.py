import unittest
from num_list import prime_number,get_primes

class TestPrime(unittest.TestCase):


    def test_prime_number(self):
        self.assertTrue(prime_number(2))
        self.assertTrue(prime_number(3))
        self.assertTrue(prime_number(13))
        self.assertFalse(prime_number(1))
        self.assertFalse(prime_number(0))
        self.assertFalse(prime_number(9))
        self.assertFalse(prime_number(100))

    def test_get_primes(self):
        self.assertEqual(get_primes([1, 2, 3, 4, 5]), [2, 3, 5])
        self.assertEqual(get_primes([6, 8, 10]), [])
        self.assertEqual(get_primes([]), [])
        self.assertEqual(get_primes([11, 13, 17]), [11, 13, 17])

if __name__ == "__main__":
    unittest.main()
