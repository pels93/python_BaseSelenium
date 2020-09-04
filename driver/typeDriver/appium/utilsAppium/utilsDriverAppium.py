import time
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction


class UtilsDriverAppium:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def sleep(self):
        time.sleep(5)

    def sleep_devices(self, indice: int = 5):
        aux = 0
        while aux < int(indice):
            time_device = int(self.get_time_phone("second"))
            if time_device != aux:
                aux += 1

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

    def get_time_phone(self, time_type: str = "second"):
        aux: str = self.driver.get_device_time()
        aux_time_type = time_type.lower()
        if aux_time_type == "year":
            return aux[:4]
        elif aux_time_type == "mouth":
            return aux[5:7]
        elif aux_time_type == "day":
            return aux[8:10]
        elif aux_time_type == "hour":
            return aux[11:13]
        elif aux_time_type == "minute":
            return aux[14:16]
        else:
            return aux[17:19]

    def drag_and_drop(self, element: WebElement, final_pos_x, final_pos_y, milliseconds: int):
        actions = TouchAction(self.driver)
        actions.long_press(element)
        actions.wait(milliseconds)
        actions.move_to(final_pos_x, final_pos_y)
        actions.release().perform()
