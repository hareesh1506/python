import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class PythonOrgSearch(unittest.TestCase):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    @classmethod
    def tearDown(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()

# # CODE2
# class Person:
#     name = []
#
#     def set_name(self, user_name):
#         self.name.append(user_name)
#         return len(self.name) - 1
#
#     def get_name(self, user_id):
#         if user_id >= len(self.name):
#             return 'There is no such user'
#         else:
#             return self.name[user_id]
#

# if __name__ == '__main__':
#     person = Person()
#     print('User Abbas has been added with id ', person.set_name('Abbas'))
#     print('User associated with id 0 is ', person.get_name(0))
#
# import unittest
#
#
# class Testing(unittest.TestCase):
#     def test_string(self):
#         a = 'some'
#         b = 'some'
#         self.assertEqual(a, b)
#
#     def test_boolean(self):
#         a = True
#         b = True
#         self.assertEqual(a, b)
#
# if __name__ == '__main__':
#     unittest.main()
