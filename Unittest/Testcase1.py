import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
class Search_Test(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    def test_youtube(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com/")
        self.driver.find_element(By.NAME,'name="search_query"').send_keys('oka laila kosam songs')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        print('title of the page is :',self.driver.title)
        print('test1 done sucessfull..')
        self.driver.close()


    # def test_google(self):
    #     self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #     self.driver.get("https://www.google.com/")
    #     self.driver.find_element(By.NAME, 'name="q"').send_keys('gaganam movie fight scene')
    #     self.driver.find_element(By.XPATH,'//*[@id="tsf"]/div[1]/div[1]/div[2]/button/div/span/svg').click()
    #
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/div[2]/a/div/div/div[3]').click()
    #
    #     self.driver.maximize_window()
    #
    #     print('title of the page is :', self.driver.title)
    #     print('test2 done sucessfull..')
    #     self.driver.close()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


