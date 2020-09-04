# submit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import *
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *

# https://www.geeksforgeeks.org/screenshot-element-method-selenium-python/?ref=rp


class UtilsWebElements:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def press_key(self, element):
        element.send_keys(Keys.RETURN)

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_elements_by_name(self, name):
        return self.driver.find_elements_by_name(name)

    def find_element_by_Id(self, id_element):
        return self.driver.find_element_by_id(id_element)

    def find_elements_by_id(self, id_element):
        return self.driver.find_elements_by_id(id_element)

    def find_element_by_css_selector(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def find_elements_by_css_selector(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def find_element_by_text_contains(self, text: str):
        return self.find_element_by_xpath("//*[contains(text(),'" + text + "')]")

    def find_element_by_text(self, text: str):
        return self.find_element_by_xpath("//*[text()='" + text + "']")

    def get_css_value(self, tag_css, web_element):
        return web_element.value_of_css_property(tag_css)

    def get_attribute(self, tag_attribute, web_element):
        return web_element.get_attribute(tag_attribute)

    def assert_equal_text(self, text1, text2, enable_error=True):
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

    def assert_containt_text(self, text1: str, text2: str, enable_error=True):
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

    def assert_not_containt_text(self, text1: str, text2: str, enable_error=True):
        if enable_error:
            Utils.print_info("INFO -> \n" +
                             text1 + "\n" + text2)
            assert (text1.find(text2) == -1)
        else:
            Utils.print_info("INFO -> EQUALS\n" +
                             text1 + "\n" + text2)
            try:
                assert (text1.find(text2) == -1)
            except:
                pass


    def assert_is_display_or_enable(self, element, enable_error=True):

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

    def assert_is_not_display(self, element, enable_error=True):
        point_y = element.location['y']
        point_x = element.location['x']
        if enable_error:
            assert (point_y < 0 or point_x < 0)
        else:
            try:
                assert (point_y < 0 or point_x < 0)
            except:
                Utils.print_info("WARNING -> is Displayed the element " + element)

