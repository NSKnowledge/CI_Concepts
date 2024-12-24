import unittest
from app import add, mul


class TestMathFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20),30)
        self.assertEqual(add(-10, 5), -5)

    def test_mul(self):
        self.assertEqual(mul(2, 6), 12)
        self.assertEqual(mul(-6, 6), -36)


if __name__=='__main__':
    unittest.main()