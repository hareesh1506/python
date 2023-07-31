from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time



class Googlesearch(unittest.TestCase):
    def test_search_twitter(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('https://google.com')
        self.driver.find_element(By.NAME, "q").clear()
        time.sleep(3)
        self.driver.find_element(By.NAME, "q").send_keys('twitter')
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.NAME, "btnK").click()
        print('test1 passed')




    def test_search_instagram(self):
        self.driver.get('https://google.com')
        self.driver.find_element(By.NAME, "q").clear()
        time.sleep(3)
        self.driver.find_element(By.NAME, "q").send_keys('instagram')
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.NAME, "btnK").click()
        print('test2 passed')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     print('TEST COMPLETED..')

# if __name__ == '__main__':
#     unittest.main()


