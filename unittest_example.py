import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 93), 8)
        
    def test_add_postive(self):
        self.assertEqual(add(5, 3), 8)
        
    def test_add_negativ(self):
        self.assertEqual(add(5, 3), -8)

if __name__ == '__main__':
    unittest.main()
