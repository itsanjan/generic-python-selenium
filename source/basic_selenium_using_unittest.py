import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    # def test_search_in_python_org(self):
    #     driver = self.driver
    #     driver.get("http://www.python.org")
    #     self.assertIn("Python", driver.title)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     assert "No results found." not in driver.page_source

    def test_dropdown_read(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        self.assertIn("Facebook", driver.title)
        birthday_month_dropdown = Select(driver.find_element(By.ID, 'month'))

        # for i in birthday_month_dropdown:
        #     print(birthday_month_dropdown.text)

        #print (birthday_month_dropdown.first_selected_option.text)

        birthday_month_dropdown_xpath = driver.find_elements(By.XPATH,'//select[@id="month"]/option')

        for n in range(len(birthday_month_dropdown_xpath)):
            print(birthday_month_dropdown_xpath[n].text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

"""
Selenium provides the following methods to locate elements in a page:

find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

To find multiple elements (these methods will return a list):

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector

Generic private method :

from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')

These are the attributes available for By class:

ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
https://selenium-python.readthedocs.io/locating-elements.html
"""