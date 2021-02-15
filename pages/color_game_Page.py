import sys
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from driver.typeDriver.selenium.selenium import *


class ColorGames:

    def __init__(self, seleium):
        sys.setrecursionlimit(999999)
        self.selenium: Selenium = seleium
        self.start_game()
        self.selenium.utilsDriver.wait(1)

    def start_game(self):
        start: WebElement = self.selenium.driver.find_element_by_class_name("main").click()
        self.start_game()

