# sleep
from selenium.webdriver import ActionChains
import time


class UtilsDriverSelenium():

    def __init__(self, driver):
        self.driver = driver

    def sleep(self, seconds):
        time.sleep(seconds)

    def close(self):
        self.driver.close

    def quit(self):
        self.driver.quit

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def browser_go_to(self, url):
        self.driver.get(url)

    def get_browser_url(self):
        return str(self.driver.current_url)

    def move_element_by_position(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).release().perform()

    def click_long(self, element):
        action = ActionChains(self.driver)
        action.click_and_hold(element).release().perform()

    def click_clickposition(self, posx, posy):
        action = ActionChains(self.driver)
        action.move_by_offset(posx, posy).release().perform()

    def click_button_right(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).release().perform()

    def click_double(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).release().perform()

    def move_element_by_position(self, element):
        width = element.size["width"]
        action = ActionChains(self.driver)
        action.move_by_offset((width / 2) - 2, 0).release().perform()

    def move_element_by_position_and_click(self, element):
        width = element.size["width"]
        action = ActionChains(self.driver)
        action.move_by_offset((width / 2) - 2, 0).click().release().perform()

    def scroll(self, pos_y):
        self.driver.execute_script("window.scrollBy(0," + pos_y + ")")
