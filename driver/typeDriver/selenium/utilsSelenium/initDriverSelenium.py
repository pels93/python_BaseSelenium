from selenium import webdriver
from driver.typeDriver.interfaces.dictionary_driver import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#   https://pypi.org/project/webdriver-manager/
class StartDriverSelenium:

    @staticmethod
    def start_browser(browser):
        if browser == firefox:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == edge:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser == iexplorer:
            driver = webdriver.Ie(IEDriverManager().install())
        elif browser == opera:
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        elif browser == safari:
            driver = webdriver.Safari()
        else:  # Chrome
            # enable get log console
            d = DesiredCapabilities.CHROME
            d['loggingPrefs'] = {'browser': 'ALL'}
            driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=d)
        return driver
