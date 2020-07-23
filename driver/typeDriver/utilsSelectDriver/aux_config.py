from driver.typeDriver.utilsSelectDriver.config import *
from driver.typeDriver.interfaces.dictionary_driver import *


class ReadConfig:

    @staticmethod
    def get_type_driver():
        tag = "typeDriver"
        aux = ReadConfig._value_tag_(tag).lower()
        if aux.find("p") > 0:
            settings[tag] = appium
        else:
            settings[tag] = selenium
        return str(settings[tag])

    @staticmethod
    def get_browser():
        tag = 'typeBrowser'
        aux = ReadConfig._value_tag_(tag).lower()
        if aux.find("ed") > -1:
            settings[tag] = edge
        elif aux.find("sa") > -1:
            settings[tag] = safari
        elif aux.find("p") > -1:
            settings[tag] = opera
        elif aux.find("f") > -1:
            settings[tag] = firefox
        elif aux.find("ex") > -1:
            settings[tag] = explorer
        else:
            settings[tag] = chrome
        return str(settings[tag])

    @staticmethod
    def get_enable_delete_old_driver():
        tag = 'enableDeleteOldDrivers'
        aux = ReadConfig._value_tag_(tag).lower()
        if aux.find("t") > -1:
            settings[tag] = True
        else:
            settings[tag] = False
        return str(settings[tag])

    @staticmethod
    def get_mobile_platform():
        tag = 'mobilePlatform'
        aux = ReadConfig._value_tag_(tag).lower()
        if aux.find("a") > -1:
            settings[tag] = android
        else:
            settings[tag] = ios
        return str(settings[tag])

    @staticmethod
    def get_mobile_version():
        return ReadConfig._value_tag_('versionMobile').lower()

    @staticmethod
    def get_mobile_name():
        return ReadConfig._value_tag_('nameMobile')

    @staticmethod
    def get_mobile_name_adb():
        return ReadConfig._value_tag_('adbName')

    @staticmethod
    def get_mobile_language():
        return ReadConfig._value_tag_('mobileLanguage')

    @staticmethod
    def get_mobile_app():
        return ReadConfig._value_tag_('app')

    @staticmethod
    def _value_tag_(tag):
        try:
            aux = str(settings[tag])
        except:
            aux = ""
        return aux
