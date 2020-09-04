import time

from behave import Given, When, Then
from driver.typeDriver.selenium.selenium import *

# mod selenium
selenium: Selenium
driver: WebDriver


@Given('imprimir logs consola')
@When('imprimir logs consola')
@Then('imprimir logs consola')
def start_brower(context):
    time.sleep(3)
    global selenium, driver
    selenium = context.type_driver
    driver = selenium.driver
    Utils.print_info("Error force for print log browser")
    for entry in driver.get_log('browser'):
        print(entry)
    assert 1 == 0
