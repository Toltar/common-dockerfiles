import unittest
from main import add

class TestAdd(unittest.TestCase):
    def test(self):
        self.assertEqual(add(2,2), 4)

class TestEvaluate(unittest.TestCase):
    def test(self):
        self.assertEqual(add(3,4), 7)
 
if __name__ == '__main__':
    unittest.main()