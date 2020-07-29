# submit
from appium.webdriver.webdriver import *
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *


class UtilsMobileElements:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_elements_by_name(self, name):
        return self.driver.find_elements_by_name(name)

    def find_element_by_id(self, id_element):
        return self.driver.find_element_by_id(id_element)

    def find_elements_by_id(self, id_element):
        return self.driver.find_elements_by_id(id_element)

    def find_element_by_id_or_xpath(self, id_element, xpath):
        element = self.find_elements_by_id(id_element)
        if len(element) > 0:
            return element[0]
        else:
            return self.find_element_by_xpath(xpath)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def assert_is_display_or_enable(self, element, enable_error):

        if enable_error:
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

    def assert_equal_text(self, text1, text2, enable_error):
        if enable_error:
            Utils.print_info("INFO -> EQUALS\n" +
                             text1 + "\n" + text2)
            assert (text1 == text2)
        else:
            Utils.print_info("INFO -> EQUALS\n" +
                             text1 + "\n" + text2)
            try:
                assert (text1 == text2)
            except:
                pass

    def assert_containt_text(self, text1: str, text2: str, enable_error):
        if enable_error:
            Utils.print_info("INFO -> \n" +
                             text1 + "\n" + text2)
            assert (text1.find(text2) > -1)
        else:
            Utils.print_info("INFO -> EQUALS\n" +
                             text1 + "\n" + text2)
            try:
                assert (text1.find(text2) > -1)
            except:
                pass