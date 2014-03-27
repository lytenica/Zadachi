from solution import count_vowels
import unittest

class vowelsTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(2,count_vowels("Python"))
        self.assertEqual(8,count_vowels("A nice day to code!"))
if __name__ == '__main__':
    unittest.main()
