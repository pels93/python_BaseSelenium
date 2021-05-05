from driver.typeDriver.interfaces.dictionary_driver import *
from driver.typeDriver.selenium.utilsSelenium.wrapperDrivers.edge import Edge
from driver.typeDriver.selenium.utilsSelenium.wrapperDrivers.firefox import Firefox
from driver.typeDriver.selenium.utilsSelenium.wrapperDrivers.ie import internetExplorer
from driver.typeDriver.selenium.utilsSelenium.wrapperDrivers.opera import Opera
from driver.typeDriver.selenium.utilsSelenium.wrapperDrivers.chrome import Chrome
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


class StartDriverSelenium:

    def __init__(self):
        # self._start_proxy_("127.0.0.1", 2321)
        pass

    def start_browser(self, browser):
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

    def _start_proxy_(self, ip: str, port: int):
        prox = Proxy()
        endpoint = ip + ":" + str(port)
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = endpoint
        prox.socks_proxy = endpoint
        prox.ssl_proxy = endpoint
