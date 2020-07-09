#sleep
from driver.typeDriver.selenium.selenium import *
import time

class utilsDriverSelenium():

    def __init__(self,driver):
        self.driver=driver

    def sleep(self,seconds):
        time.sleep(seconds)
    
    def close(self):
        self.driver.close
    
    def quit(self):
        self.driver.quit
    
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
    
    def browserGoTo(self,url):
        self.driver.get(url)
    
    def getBrowserUrl(self):
        return str(self.driver.current_url)
