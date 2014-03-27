from solution import is_prime
import unittest

class primeTest(unittest.TestCase):
    def test_isprime(self):
        self.assertEqual(False,is_prime(8))
        self.assertEqual(True,is_prime(11))
if __name__ == '__main__':
    unittest.main()
