from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
import time
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

Path="C://Program Files (x86)//chromedriver-win32//chromedriver.exe"
driver = webdriver.Chrome(Path)
# driver = webdriver.Chrome(#########################)
# code1
# """
driver.get("https://www.w3schools.com/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="search2"]').click()
time.sleep(2)
driver.close()


# """

# CODE2
"""
driver.get('https://web.whatsapp.com/')
time.sleep(25)
title=driver.title
print(title)
driver.close()
"""

# CODE
"""
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
time.sleep(4)
elem.send_keys("pycon")
time.sleep(2)

elem.send_keys(Keys.RETURN)
time.sleep(2)

# assert "No results found." not in driver.page_source
driver.close()
"""

# CODE
"""
driver.get('https://genetichealing.in/pms/hospital-management-login-page/')
driver.find_element(By.ID,'user_login').send_keys('hareesh')
time.sleep(3)
driver.find_element(By.ID,'user_pass').send_keys('password')
time.sleep(1)

radiobutton=driver.find_element(By.NAME,'rememberme')
radiobutton.click()
time.sleep(1)

login = driver.find_element(By.NAME,'wp-submit')
login.click()

driver.close()

"""

