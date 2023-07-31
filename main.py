
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(3)

f_name=driver.find_element(By.XPATH,'//*[@id="u_0_b_x5"]')
f_name.click()
pr
driver.find_element(By.
time.sleep(2)
driver.close()
