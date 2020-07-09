from selenium import webdriver
from driver.typeDriver.interfaces.dictionary_driver import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


#   https://pypi.org/project/webdriver-manager/
class StartDriverSelenium:

    @staticmethod
    def start_browser(browser):
        if browser == firefox:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == edge:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser == opera:
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        elif browser == safari:
            driver = webdriver.Safari()
        else:  # Chrome
            driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver
