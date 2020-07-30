# sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import *
import time


class UtilsDriverSelenium:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def sleep(self, seconds):
        time.sleep(seconds)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def browser_go_to(self, url):
        self.driver.get(url)

    def browser_go_to_back(self, url):
        self.driver.back()

    def get_browser_url(self):
        return str(self.driver.current_url)

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

    def move_mouse_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).release().perform()

    def hover_element(self, element):
        width = element.size["width"]
        action = ActionChains(self.driver)
        action.move_to_element(element).move_by_offset((width / 2) - 2, 0).release().perform()

    def hover_and_click_element(self, element):
        width = element.size["width"]
        action = ActionChains(self.driver)
        action.move_to_element(element).move_by_offset((width / 2) - 2, 0).click().release().perform()

    def drag_and_drop_element_to_element(self, element, element_final):
        action = ActionChains(self.driver)
        action.drag_and_drop(element, element_final).release().perform()

    def drag_and_drop_element(self, element, pos_x, pos_y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, pos_x, pos_y).release().perform()

    def scroll_y(self, pos_y):
        self.driver.execute_script("window.scrollBy(0," + pos_y + ")")
        self.sleep(2)

    def scroll_x(self, pos_x):
        self.driver.execute_script("window.scrollBy(" + pos_x + ",0)")
        self.sleep(2)

    def scroll_by_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.sleep(2)
