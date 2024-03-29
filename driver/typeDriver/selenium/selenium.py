from driver.typeDriver.utilsSelectDriver.aux_config import *
from driver.typeDriver.selenium.utilsSelenium.initDriverSelenium import StartDriverSelenium
from driver.typeDriver.selenium.utilsSelenium.utilsDriverSelenium import UtilsDriverSelenium
from driver.typeDriver.selenium.utilsSelenium.utilsWebElements import UtilsWebElements
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *
from selenium.webdriver.chrome.webdriver import *


#   https://pypi.org/project/webdriver-manager/


class Selenium:

    def __init__(self):
        self.delete_old_drivers(ReadConfig.get_enable_delete_old_driver())
        self.browser = ReadConfig.get_browser()
        driverSelenium=StartDriverSelenium()
        self.driver: WebDriver = driverSelenium.start_browser(self.browser)
        self.utilsDriver = UtilsDriverSelenium(self.driver, self.browser)
        self.utilsWebElements = UtilsWebElements(self.driver, self.browser)


    def delete_old_drivers(self, enable_delete):
        if enable_delete:
            Utils.folder_delete(Utils.merge_directory_to_folder(
                Utils.directory_user_pc(), ".wdm"))
