import unittest
import katas

__author__ = "Timothy La (tla111)"


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(5, 10), 15)
        self.assertEqual(katas.add(20, 10), 30)
        self.assertEqual(katas.add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 2), 4)
        self.assertEqual(katas.multiply(-10, 2), -20)
        self.assertEqual(katas.multiply(100, 2), 200)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)
        self.assertEqual(katas.power(10, 5), 100000)
        self.assertEqual(katas.power(20, 3), 8000)

    def test_factorial(self):
        self.assertEqual(katas.factorial(3), 6)
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(7), 5040)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(10), 34)
        self.assertEqual(katas.fibonacci(12), 89)
        self.assertEqual(katas.fibonacci(20), 4181)


if __name__ == '__main__':
    unittest.main()
