from driver.typeDriver.selenium.selenium import *


class google_Page():

    def __init__(self, aux_seleium):
        self.selenium: Selenium = aux_seleium
        self.findElements()

    def findElements(self):
        self.barra = self.selenium.utilsWebElements.find_element_by_name("q")
    # self.btnStartSesion = self.selenium.utilsWebElements.findElementByCssSelector("a#gb_70.gb_pe.gb_4.gb_5c");
