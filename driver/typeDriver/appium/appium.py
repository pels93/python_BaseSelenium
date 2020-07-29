from driver.typeDriver.utilsSelectDriver.aux_config import *
from driver.typeDriver.appium.utilsAppium.initDriverAppium import StartDriverAppium
from driver.typeDriver.appium.utilsAppium.utilsDriverAppium import utilsDriverAppium
from driver.typeDriver.appium.utilsAppium.UtilsMobileElements import UtilsMobileElements


#   https://pypi.org/project/Appium-Python-Client/
class Appium:

    def __init__(self):
        self.platform = ReadConfig.get_mobile_platform()
        self.driver = StartDriverAppium.start_driver_platform(self.platform)
        self.utilsDriver = utilsDriverAppium(self.driver)
        self.utilsMobileElements = UtilsMobileElements(self.driver)
