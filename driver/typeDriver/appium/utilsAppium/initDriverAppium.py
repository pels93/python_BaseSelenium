from selenium.webdriver import DesiredCapabilities

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
                deviceName=ReadConfig.get_mobile_name()
            )
            #TEST APP OR WEB
            if len(str(ReadConfig.get_mobile_app())) > 1:
                desired_caps.update(dict(
                    app=Utils.merge_directory_to_folder(AppsDirectory, ReadConfig.get_mobile_app())))

            else:
                desired_caps.update(dict(browserName='Safari'))
        else:
            desired_caps = dict(
                platformName='Android',
                automationName='uiautomator2',
                platformVersion=ReadConfig.get_mobile_version(),
                deviceName=ReadConfig.get_mobile_name(),
                udid=ReadConfig.get_mobile_name_adb(),
                locate=ReadConfig.get_mobile_language()
            )
            #TEST APP OR WEB
            if len(str(ReadConfig.get_mobile_app())) > 1:
                desired_caps.update(dict(
                    app=Utils.merge_directory_to_folder(AppsDirectory, ReadConfig.get_mobile_app())))
            else:
                capabilities = DesiredCapabilities.CHROME.copy()
                capabilities['acceptInsecureCerts'] = True
                capabilities['acceptSslCerts'] = True
                capabilities['ACCEPT_SSL_CERTS'] = True
                capabilities['ACCEPT_INSECURE_CERTS'] = True
                capabilities['webdriver_accept_untrusted_certs'] = True
                capabilities['webdriver_assume_untrusted_issuer'] = True
                desired_caps.update(capabilities)
                desired_caps.update(dict(browserName='Chrome'))
        driver = webdriver.Remote(str(settings['urlServerAppium']), desired_caps)
        return driver
