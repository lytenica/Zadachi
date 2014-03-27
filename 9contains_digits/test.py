from solution import contains_digits
import unittest
class digitsTest(unittest.TestCase):
    def test_digits(self):
        self.assertEqual(True,contains_digits(402123, [0, 3, 4]))
        self.assertEqual(False,contains_digits(666, [6,4]))
if __name__ == '__main__':
    unittest.main()
