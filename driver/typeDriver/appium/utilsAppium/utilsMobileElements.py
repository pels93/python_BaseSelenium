# submit
from appium.webdriver.webdriver import *

from driver.typeDriver.appium.utilsAppium.utilsDriverAppium import UtilsDriverAppium
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *


class UtilsMobileElements:

    def __init__(self, driver):
        self.utilsDriver: UtilsDriverAppium = UtilsDriverAppium(driver)
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

    def find_elements_by_xpath(self, xpath: str, seconds):
        self.utilsDriver.wait(seconds)
        return self.driver.find_elements_by_xpath(xpath)

    def find_element_by_text_contains(self, text: str):
        return self.find_element_by_xpath("//*[contains(text(),'" + text + "')]")

    def find_elements_by_text_contains(self, text: str, seconds):
        return self.find_elements_by_xpath("//*[contains(text(),'" + text + "')]", seconds)

    def text_is_not_present(self, text: str, seconds) -> bool:
        aux = self.find_elements_by_xpath("//*[contains(text(),'" + text + "')]", seconds)
        if len(aux) > 0:
            return True
        else:
            return False

    def find_element_by_text(self, text: str):
        return self.find_element_by_xpath("//*[text()='" + text + "']")

    def find_elements_by_text(self, text: str, seconds):
        return self.find_elements_by_xpath("//*[text()='" + text + "']", seconds)

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
        Utils.print_info("INFO -> EQUALS\n" +
                         text1 + "\n" + text2)
        aux_return = False
        if enable_error:
            if text1 == text2:
                aux_return = True
            elif text1.find(text2) > -1:
                aux_return = True
            assert aux_return
        else:
            if text1 == text2:
                aux_return = True
            elif text1.find(text2) > -1:
                aux_return = True

        return aux_return

    def assert_not_containt_text(self, text1: str, text2: str, enable_error=True) -> bool:
        aux_return = False
        Utils.print_info("INFO -> EQUALS\n" +
                         text1 + "\n" + text2)
        if enable_error:
            if text1.find(text2) == -1:
                aux_return = True
            assert aux_return
        else:
            if text1.find(text2) == -1:
                aux_return = True
        return aux_return

    def assert_is_display_or_not_in_element(self, element, element_container, is_display=True, enable_error=True):
        point_y = element.location['y']
        point_x = element.location['x']
        element_container_y_top = element_container.location['y']
        element_container_y_down = element_container_y_top + element_container.size["height"]
        element_container_x_left = element_container.location['x']
        element_container_x_right = element_container_x_left + element_container.size["width"]

        if enable_error:
            assert ((element_container_x_left < point_x) and (element_container_x_right > point_x) and (
                    element_container_y_top < point_y) and (element_container_y_down > point_y)) == is_display
        else:
            try:
                assert ((element_container_x_left < point_x) and (element_container_x_right > point_x) and (
                        element_container_y_top < point_y) and (element_container_y_down > point_y)) == is_display

            except:
                Utils.print_info("WARNING -> is Displayed the element " + element)
