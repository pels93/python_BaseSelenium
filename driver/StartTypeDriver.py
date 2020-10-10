from driver.typeDriver.utilsSelectDriver.aux_config import *
from driver.typeDriver.selenium.selenium import Selenium
from driver.typeDriver.appium.appium import Appium
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *
from driver.typeDriver.interfaces.dictionary_driver import *
from driver.typeDriver.utilsSelectDriver.config import settings

name_folder_screen = "ScreenShot"


def delete_old_report():
    if settings['enableDeleteOldReport']:
        Utils.folder_delete(name_folder_screen)


class StartDriver:
    def __init__(self):
        self.typeDriverStr = str(ReadConfig.get_type_driver()).lower()
        if self.typeDriverStr == appium:
            self.typeDriver = Appium()
        else:
            self.typeDriver = Selenium()

    def scenario_end(self):
        self.typeDriver.driver.quit()

    def scenario_fail(self, scenario, step, date):
        directory_screen = Utils.merge_directory_to_folder(
            Utils.folder_proyect(), name_folder_screen)
        Utils.folder_create(directory_screen)
        if self.typeDriverStr == appium:
            directory_screen_final = Utils.merge_directory_to_folder(Utils.merge_directory_to_folder(
                Utils.merge_directory_to_folder(Utils.merge_directory_to_folder(
                    directory_screen, date), self.typeDriverStr), ReadConfig.get_mobile_platform()),
                scenario)
        else:
            directory_screen_final = Utils.merge_directory_to_folder(Utils.merge_directory_to_folder(
                Utils.merge_directory_to_folder(Utils.merge_directory_to_folder(
                    directory_screen, date), self.typeDriverStr), ReadConfig.get_browser()),
                scenario)
        self._screenshot_(Utils.folders_create_tree(directory_screen, directory_screen_final), step)

    def _screenshot_(self, directory_screen, step):
        namefile = Utils.folder_validate_name(step) + ".png"
        ruta = directory_screen + "\\" + namefile
        self.typeDriver.driver.save_screenshot(ruta)
        if Utils.folder_exists(ruta):
            Utils.print_info("INFO-> ScreenShot saved in \n" + ruta)
        else:
            Utils.print_info("WARNING-> ScreenShot NOT saved in \n" + ruta)
