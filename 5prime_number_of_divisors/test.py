from solution import prime_number_of_divisors
import unittest

class pdivisors(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(True,prime_number_of_divisors(28))
        self.assertEqual(True,prime_number_of_divisors(9))
if __name__ == '__main__':
    unittest.main()
