import unittest
from selenium import webdriver

class TestWebPage(unittest.TestCase):
    def setUp(self):
        # Create a new Chrome driver instance before each test method
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Quit the driver after each test method
        self.driver.quit()

    def test_page_title(self):
        # Open the web page
        self.driver.get('https://www.google.com')

        # Get the title of the page
        title = self.driver.title

        # Assert that the title is correct
        self.assertEqual(title, 'google ')
