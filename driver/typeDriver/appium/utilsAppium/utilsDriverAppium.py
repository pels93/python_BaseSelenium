#sleep
from driver.typeDriver.selenium.selenium import *
import time

class utilsDriverAppium():

    def __init__(self,driver):
        self.driver=driver

    def sleep(self):
        time.sleep(5)
    
    def close(self):
        self.driver.close
    
    def quit(self):
        self.driver.quit
    
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
    