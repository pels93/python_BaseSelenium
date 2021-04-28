from selenium import webdriver
from driver.typeDriver.interfaces.dictionary_driver import *

from driver.typeDriver.selenium.utilsSelenium.listWebDrivers.edge import Edge
from driver.typeDriver.selenium.utilsSelenium.listWebDrivers.firefox import Firefox
from driver.typeDriver.selenium.utilsSelenium.listWebDrivers.ie import internetExplorer
from driver.typeDriver.selenium.utilsSelenium.listWebDrivers.opera import Opera
from driver.typeDriver.selenium.utilsSelenium.listWebDrivers.chrome import Chrome


class StartDriverSelenium:

    @staticmethod
    def start_browser(browser):
        if browser == firefox:
            firefox_webdriver = Firefox()
            driver = firefox_webdriver.start()
        elif browser == edge:
            edge_webdriver = Edge()
            driver = edge_webdriver.start()
        elif browser == iexplorer:
            explorer = internetExplorer()
            driver = explorer.start()
        elif browser == opera:
            opera_webdriver = Opera()
            driver = opera_webdriver.start()
        elif browser == safari:
            driver = webdriver.Safari()
        else:  # Chrome
            chrome_webdriver = Chrome()
            driver = chrome_webdriver.start()
        return driver
