import unittest
import calc
import katas

__author__ = "Timothy La (tla111)"


class TestKatas(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_multiply(self):
        self.fail("TODO: Write multiply unit test")

    def test_power(self):
        self.fail("TODO: Write power unit test")

    def test_factorial(self):
        self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
