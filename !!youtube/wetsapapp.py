import pywhatkit as hari
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# import unittest
#
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
hari.sendwhatmsg('+916281110995','hii ra',12,6)
hari.playonyt('swing zara song')



class TestWebPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        # Create a new Chrome driver instance before each test method
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    def tearDown(self):
        # Quit the driver after each test method
        self.driver.quit()

    def test_watsap_mesg(self):
        # Open the web page
        self.driver.get('https://www.google.com')

        # Get the title of the page
        title = self.driver.title

        # Assert that the title is correct
        self.assertEqual(title, 'google ')



























# hari.playonyt('chitti nadumune chustuna song')
# hari.search('python automation')