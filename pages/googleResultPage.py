from driver.typeDriver.selenium.selenium import *
class google_result_search():

    def __init__(self, aux_seleium):
        self.selenium: Selenium = aux_seleium
        self.findElements()

    def findElements(self):
        self.resultFirst = self.selenium.utilsWebElements.find_element_by_css_selector(".r a")
