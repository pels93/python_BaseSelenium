from driver.typeDriver.utilsSelectDriver.aux_config import *
from appium import webdriver
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *
from driver.typeDriver.interfaces.dictionary_driver import *


#   https://pypi.org/project/Appium-Python-Client/
class StartDriverAppium:

    @staticmethod
    def start_driver_platform(platform):
        AppsDirectory = Utils.merge_directory_to_folder(Utils.folder_proyect(), "resources")
        if platform == ios:
            desired_caps = dict(
                platformName='iOS',
                platformVersion=ReadConfig.get_mobile_version(),
                automationName='xcuitest',
                deviceName=ReadConfig.get_mobile_name(),
                app=Utils.merge_directory_to_folder(AppsDirectory, ReadConfig.get_mobile_app())
            )
        else:
            desired_caps = dict(
                platformName='Android',
                platformVersion=ReadConfig.get_mobile_version(),
                deviceName=ReadConfig.get_mobile_name(),
                udid=ReadConfig.get_mobile_name_adb(),
                locate=ReadConfig.get_mobile_language(),
                app=Utils.merge_directory_to_folder(AppsDirectory, ReadConfig.get_mobile_app())

            )
        driver = webdriver.Remote(str(settings['urlServerAppium']), desired_caps)
        return driver
