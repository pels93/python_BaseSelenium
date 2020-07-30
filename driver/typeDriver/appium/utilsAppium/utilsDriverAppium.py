from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
import time


class UtilsDriverAppium:

    def __init__(self, driver):
        self.driver = driver

    def sleep(self):
        time.sleep(5)

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def press_long_element(self, element: WebElement, milliseconds: int):
        actions = TouchAction(self.driver)
        actions.press(element)
        actions.wait(milliseconds)
        actions.release().perform()

    def press_long_position(self, pos_x, pos_y, milliseconds: int):
        actions = TouchAction(self.driver)
        actions.wait(milliseconds)
        actions.press(pos_x, pos_y).release().perform()

    def swipe(self, ini_pos_x, ini_pos_y, final_pos_x, final_pos_y, milliseconds: int):
        actions = TouchAction(self.driver)
        actions.press(ini_pos_x, ini_pos_y)
        actions.wait(milliseconds)
        actions.move_to(final_pos_x, final_pos_y)
        actions.release().perform()

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def get_time_phone(self):
        self.driver.get_device_time()

    def drag_and_drop(self, element: WebElement, final_pos_x, final_pos_y, milliseconds: int):
        actions = TouchAction(self.driver)
        actions.long_press(element)
        actions.wait(milliseconds)
        actions.move_to(final_pos_x, final_pos_y)
        actions.release().perform()
