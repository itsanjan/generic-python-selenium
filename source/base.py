from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import os

# ENV_CWD = os.getcwd()
# OUTPUT_LOG_SELENIUM = ENV_CWD + '\output' + '\selenium.log'
# print(OUTPUT_LOG_SELENIUM)
# TEST_EXECUTION_BROWSER = 'chrome'

# def create_selenium_driver(browser='chrome'):
#     if browser == 'chrome':
#         return webdriver.Chrome(
#             service_args=["--verbose", "--log-path="+OUTPUT_LOG_SELENIUM]
#         )
#     elif browser == 'firefox':
#         return webdriver.Firefox()
#     elif browser == 'marionette':
#         capabilities = DesiredCapabilities.FIREFOX
#         capabilities['marionette'] = True
#         return webdriver.Firefox(capabilities=capabilities)
#     elif browser == 'ie':
#         return webdriver.Ie()
#     elif browser == 'phantomjs':
#         return webdriver.PhantomJS()
#     else:
#         msg = 'Selenium driver for browser %s is not available' % browser
#         raise RuntimeError(msg) 

# driver = create_selenium_driver(TEST_EXECUTION_BROWSER)
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

#Keeping the project simple so that the library methods sticks in my head
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()