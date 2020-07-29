from appium.webdriver.webdriver import *
from appium.webdriver.common.touch_action import TouchAction
import time


class utilsDriverAppium:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def sleep(self):
        time.sleep(5)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

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
        self.driver.get_device_time()