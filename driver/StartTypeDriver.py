from driver.typeDriver.utilsSelectDriver.aux_config import *
from driver.typeDriver.selenium.selenium import Selenium
from driver.typeDriver.appium.appium import Appium
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *
from driver.typeDriver.interfaces.dictionary_driver import *


class StartDriver:
    def __init__(self):
        self.typeDriver = ReadConfig.get_type_driver()
        if self.typeDriver == appium:
            self.appium = Appium()
        else:
            self.selenium = Selenium()

    def scenario_end(self):
        self.get_driver().driver.quit()

    def scenario_fail(self, scenario, step, date):
        name_folder_screen = "ScreenShot"
        directory_screen = Utils.merge_directory_to_folder(
            Utils.folder_proyect(), name_folder_screen)
        Utils.folder_create(directory_screen)
        if self.typeDriver == appium:
            directory_screen_final = Utils.merge_directory_to_folder(Utils.merge_directory_to_folder(
                Utils.merge_directory_to_folder(Utils.merge_directory_to_folder(
                    directory_screen, date), self._get_driver_name_()), ReadConfig.get_mobile_platform()),
                scenario)
        else:
            directory_screen_final = Utils.merge_directory_to_folder(Utils.merge_directory_to_folder(
                Utils.merge_directory_to_folder(Utils.merge_directory_to_folder(
                    directory_screen, date), self._get_driver_name_()), ReadConfig.get_browser()),
                scenario)
        self._screenshot_(Utils.folders_create_tree(directory_screen, directory_screen_final), step)

    def get_driver(self):
        if self.typeDriver == appium:
            return self.appium
        else:
            return self.selenium

    def _get_driver_name_(self):
        if self.typeDriver == appium:
            return appium
        else:
            return selenium

    def _screenshot_(self, directory_screen, step):
        namefile = Utils.folder_validate_name(step) + ".png"
        ruta = directory_screen + "\\" + namefile
        self.get_driver().driver.save_screenshot(ruta)
        if Utils.folder_exists(ruta):
            Utils.print_info("INFO-> ScreenShot saved in \n" + ruta)
        else:
            Utils.print_info("WARNING-> ScreenShot NOT saved in \n" + ruta)
