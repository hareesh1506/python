import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Calculator class before each test method
        self.calc = Calculator()


    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        print(result)

    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)
        print(result)

    def test_multiply(self):
        result = self.calc.multiply(2, 4)
        self.assertEqual(result, 8)
        print(result)

    def test_divide(self):
        result = self.calc.divide(10, 5)
        self.assertEqual(result, 2)
        print(result)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
