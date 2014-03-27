from solution import count_consonants
import unittest

class consonantsTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(4,count_consonants("Python"))
        self.assertEqual(6,count_consonants("A nice day to code!"))
if __name__ == '__main__':
    unittest.main()
