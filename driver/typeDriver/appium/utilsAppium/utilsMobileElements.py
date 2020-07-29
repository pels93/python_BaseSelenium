# submit
from appium.webdriver.webdriver import *
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *


class utilsMobileElements:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def findElementByName(self, name):
        return self.driver.find_element_by_name(name)

    def findElementsByName(self, name):
        return self.driver.find_elements_by_name(name)

    def findElementById(self, id):
        return self.driver.find_element_by_id(id)

    def findElementsById(self, id):
        return self.driver.find_elements_by_id(id)

    def findElementByIdOrXpath(self, id, xpath):
        element = self.findElementsById(id)
        if(len(element) > 0):
            return element[0]
        else:
            return self.findElementByXPath(xpath)

    def findElementByXPath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def findElemenstByXPath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def assertIsDisplayOrEnanble(self, element, enableError):

        if (enableError):
            element.is_displayed()
            element.is_enabled()
        else:
            try:
                element.is_displayed()
            except:
                Utils.print_info("WARNING -> is NOT Displayed the element " + element)
            try:
                element.is_enabled()
            except:
                Utils.print_info("WARNING -> is NOT enable the element " + element)

    def assertqualText(self, text1, text2, enableError):
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
                pass


