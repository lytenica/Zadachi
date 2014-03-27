from solution import is_int_palindrom
import unittest

class palindromTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(True,is_int_palindrom(1))

        self.assertEqual(False,is_int_palindrom(123))

if __name__ == '__main__':
    unittest.main()
