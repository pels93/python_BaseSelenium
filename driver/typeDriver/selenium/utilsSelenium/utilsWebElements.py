# submit
from selenium.webdriver.common.keys import Keys
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *

# https://www.geeksforgeeks.org/screenshot-element-method-selenium-python/?ref=rp


class utilsWebElements():

    def __init__(self, driver):
        self.driver = driver

    def pressKey(self, element):
        element.send_keys(Keys.RETURN)

    def findElementByName(self, name):
        return self.driver.find_element_by_name(name)

    def findElementsByName(self, name):
        return self.driver.find_elements_by_name(name)

    def findElementById(self, id):
        return self.driver.find_element_by_id(id)

    def findElementsById(self, id):
        return self.driver.find_elements_by_id(id)

    def findElementByCssSelector(self, CssSelector):
        return self.driver.find_element_by_css_selector(CssSelector)

    def findElementsByCssSelector(self, CssSelector):
        return self.driver.find_elements_by_css_selector(CssSelector)

    def findElementByXpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def findElementsByXpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def assertEqualText(self, text1, text2, enableError):
        if (enableError):
            Utils.print_info("INFO -> EQUALS\n" +
                             text1 + "\n" + text2)
            assert(text1 == text2)
        else:
            Utils.print_info("INFO -> EQUALS\n" +
                             text1 + "\n" + text2)
            try:
                assert(text1 == text2)
            except:
                None
