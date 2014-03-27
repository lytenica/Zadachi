from solution import sum_of_digits
import unittest

class sumTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(2.5,sum_of_digits(5/2))
        self.assertEqual(2,sum_of_digits(5//2))
if __name__ == '__main__':
    unittest.main()
