from solution import sum_of_divisors
import unittest

class divisorsTest(unittest.TestCase):
    def test_sum_of_divisors(self):
        self.assertEqual(15,sum_of_divisors(8))
        self.assertEqual(8,sum_of_divisors(7))
if __name__ == '__main__':
    unittest.main()
