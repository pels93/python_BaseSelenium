# submit
from driver.typeDriver.appium.appium import *
from appium.webdriver.common.touch_action import TouchAction
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *


class utilsMobileElements():

    def __init__(self, driver):
        self.driver = driver

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

    def pressLongElement(self, element, milliseconds):
        actions = TouchAction(self.driver)
        actions.press(element)
        actions.wait(milliseconds)
        actions.release().perform()

    def pressLongPosition(self, posX, posY, milliseconds):
        actions = TouchAction(self.driver)
        actions.press(x=posX, y=posY).release().perform()

    def swipe(self, iniPosX, iniPposY, FinalPosX, FinalPosY, milliseconds):
        actions = TouchAction(self.driver)
        actions.press(x=iniPosX, y=iniPposY)
        actions.wait(milliseconds)
        actions.move_to(x=FinalPosX, y=FinalPosY)
        actions.release().perform()

    def hideKeyboard(self):
        self.driver.hide_keyboard()

    def getTimePhone(self):
        Appium.driver.get_device_time()
