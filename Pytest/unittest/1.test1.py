import unittest

# The class representing the tests
class MathFunctionsTest(unittest.TestCase):

    # Setup method - executed before each test method
    def setUp(self):
        # Initialize any required resources or variables
        self.x = 10
        self.y = 5

    # Teardown method - executed after each test method
    def tearDown(self):
        # Clean up any resources used by the tests
        pass

    # Test method - starts with the word 'test'
    def test_addition(self):
        # Test the addition function
        result = self.x + self.y
        self.assertEqual(result, 15)  # Check if the result is equal to 15
        print('TEST -1 PASSED')

    def test_subtraction(self):
        # Test the subtraction function
        result = self.x - self.y
        self.assertEqual(result, 5)  # Check if the result is equal to 5
        print('TEST -2 PASSED')
        print('TEST-1 PASS')

    def test_multiplication(self):
        # Test the multiplication function
        result = self.x * self.y
        self.assertEqual(result, 50)  # Check if the result is equal to 50
        print('TEST -3 PASSED')

    def test_division(self):
        # Test the division function
        result = self.x / self.y
        self.assertEqual(result, 2)  # Check if the result is equal to 2
        print('TEST -4 PASSED')


# Run the tests
if __name__ == '__main__':
    unittest.main()
