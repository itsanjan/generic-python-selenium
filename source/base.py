from settings import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def set_logging_variable():
    global OUTPUT_LOG_SELENIUM, TEST_EXECUTION_BROWSER
    OUTPUT_LOG_SELENIUM = ENV_CWD + '\\output' + '\\selenium.log'
    TEST_EXECUTION_BROWSER = 'chrome'


def create_selenium_driver(browser='chrome'):
    if browser == 'chrome':
        return webdriver.Chrome(
            service_args=["--verbose", "--log-path="+OUTPUT_LOG_SELENIUM]
        )
    elif browser == 'firefox':
        return webdriver.Firefox()
    elif browser == 'marionette':
        capabilities = DesiredCapabilities.FIREFOX
        capabilities['marionette'] = True
        return webdriver.Firefox(capabilities=capabilities)
    elif browser == 'ie':
        return webdriver.Ie()
    elif browser == 'phantomjs':
        return webdriver.PhantomJS()
    else:
        msg = 'Selenium driver for browser %s is not available' % browser
        raise RuntimeError(msg)


set_logging_variable()
