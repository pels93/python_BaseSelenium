from driver.typeDriver.selenium.selenium import *


class GooglePageObject():

    def __init__(self, seleium):
        self.selenium: Selenium = seleium
        self.find_elements()

    def find_elements(self):
        self.barra = self.selenium.utilsWebElements.find_element_by_name("q")
    # self.btnStartSesion = self.selenium.utilsWebElements.findElementByCssSelector("a#gb_70.gb_pe.gb_4.gb_5c");
