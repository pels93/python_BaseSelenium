from setuptools import setup

setup(
    name='python_BaseSelenium',
    version='1.0.0',
    packages=['pages', 'driver', 'driver.typeDriver', 'driver.typeDriver.appium',
              'driver.typeDriver.appium.utilsAppium', 'driver.typeDriver.selenium',
              'driver.typeDriver.selenium.utilsSelenium', 'driver.typeDriver.interfaces',
              'driver.typeDriver.utilsSelectDriver', 'features', 'features.steps'],
    install_requires=['behave', 'selenium','webdriver_manager','Appium-Python-Client',
                      'Django==3.0.7'],
    author='danigonz',
    description=''
)
