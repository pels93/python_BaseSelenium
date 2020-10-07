from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import *
import time

from selenium.webdriver.remote.webelement import WebElement


class UtilsDriverSelenium:

    def __init__(self, driver, type_browser):
        self.driver: WebDriver = driver
        self.typeBrowser  = type_browser

    def sleep(self, seconds):
        time.sleep(seconds)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def delete_cache(self):
        self.driver.delete_all_cookies()

    def browser_go_to(self, url):
        self.driver.get(url)

    def browser_go_to_back(self):
        self.driver.back()

    def browser_refresh(self):
        self.driver.refresh()

    def browser_go_to_forward(self):
        self.driver.forward()

    def get_browser_url(self):
        return str(self.driver.current_url)

    def browser_get_size_windows(self, mode):
        aux = str(self.driver.get_window_size())
        if mode.lower() == "width":
            return int(aux[(aux.index(':') + 1):aux.index(',')])
        else:
            return int(aux[(aux.rindex(':') + 1):aux.index('}')])

    def browser_get_size_view(self, mode):
        if mode.lower() == "width":
            return int(self.driver.execute_script("return screen.width"))
        else:
            return int(self.driver.execute_script("return screen.height"))

    def move_element_by_position(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).release().perform()

    def click(self, element: WebElement):
        if str(self.typeBrowser).lower() == 'iexplore':
            self.driver.execute_script("return document.body.scrollHeight")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def click_long(self, element):
        action = ActionChains(self.driver)
        action.click_and_hold(element).release().perform()

    def click_element_aux(self, element):
        action = ActionChains(self.driver)
        action.click(element).release().perform()

    def click_click_position(self, pos_x, pos_y):
        action = ActionChains(self.driver)
        action.move_by_offset(pos_x, pos_y).click().release().perform()

    def click_button_right(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).release().perform()

    def click_double(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).release().perform()

    def hover_element(self, element):
        width = element.size["width"]
        action = ActionChains(self.driver)
        action.move_to_element(element).move_by_offset((width / 2) - 2, 0) \
            .release().perform()

    def hover_element_and_click(self, element):
        width = element.size["width"]
        action = ActionChains(self.driver)
        action.move_to_element(element).move_by_offset((width / 2) - 2, 0) \
            .click().release().perform()

    def scroll_y(self, pos_y):
        self.driver.execute_script("window.scrollBy(0," + pos_y + ")")
        self.sleep(2)

    def scroll_x(self, pos_x):
        self.driver.execute_script("window.scrollBy(" + pos_x + ",0)")
        self.sleep(2)

    def scroll_by_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.sleep(2)

    def drag_and_drop_element_to_element(self, element, element_final):
        action = ActionChains(self.driver)
        action.drag_and_drop(element, element_final).release().perform()

    def drag_and_drop_element(self, element, pos_x, pos_y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, pos_x, pos_y).release().perform()

    def drag_and_drop_div(self, element, pos_x=0, pos_y=0):
        # https://github.com/SeleniumHQ/selenium/issues/3269
        element_body: WebElement = self.driver.find_element_by_css_selector("body")
        c_pixel = element.size["height"] * 0.80

        aux_pos_x = int(pos_x / c_pixel)
        aux_pos_y = int(pos_y / c_pixel)

        if aux_pos_x < 0:
            count_for_x = aux_pos_x * (-1)
            aux_pos_x = -c_pixel
        elif aux_pos_x == 0:
            aux_pos_x = c_pixel
            count_for_x = 0
        else:
            # need more size for effect css
            c_pixel = element.size["width"] * 0.80
            aux_pos_x = c_pixel
            count_for_x = aux_pos_x

        if aux_pos_y < 0:
            count_for_y = aux_pos_y * (-1)
            aux_pos_y = -c_pixel
        elif aux_pos_y == 0:
            count_for_y = 0
        else:
            aux_pos_y = c_pixel
            count_for_y = aux_pos_y

        if count_for_x > count_for_y:
            aux_count = int(count_for_x)
        else:
            aux_count = int(count_for_y)

        action = ActionChains(self.driver)
        if self.typeBrowser == "firefox":
            for y in range(aux_count):
                action.click_and_hold(element).move_by_offset(aux_pos_x, aux_pos_y).release()
        else:
            for y in range(aux_count):
                action.click_and_hold(element).move_by_offset(aux_pos_x, aux_pos_y).release(element_body).release()

        action.perform()

    def open_new_tab(self):
        self.driver.execute_script("window.open()")

    def change_tab(self, index: int):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def count_tabs(self):
        return len(self.driver.window_handles)

    def close_tab(self):
        self.close()

    def set_viewport_size(self, width, height):
        window_size = self.driver.execute_script("""
            return [window.outerWidth - window.innerWidth + arguments[0],
              window.outerHeight - window.innerHeight + arguments[1]];
            """, width, height)
        self.driver.set_window_size(*window_size)
