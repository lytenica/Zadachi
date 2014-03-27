from solution import is_number_balanced
import unittest

class numberTest(unittest.TestCase):
    def test_nbalanced(self):
         self.assertEqual(True,is_number_balanced(9))
         self.assertEqual(False,is_number_balanced(13))
if __name__ == '__main__':
    unittest.main()
