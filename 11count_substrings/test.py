from solution import count_substrings
import unittest

class csubstrings(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(2,count_substrings("This is a test string", "is"))
        self.assertEqual(0,count_substrings("We have nothing in common!", "really?"))
if __name__ == '__main__':
    unittest.main()

