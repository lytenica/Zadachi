from solution import contains_digit
import unittest

class digitTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(False,contains_digit(123, 4))
        self.assertEqual(True,contains_digit(42, 2))
if __name__ == '__main__':
    unittest.main()
