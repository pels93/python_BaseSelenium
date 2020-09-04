import time

from behave import Given, When, Then
from driver.typeDriver.selenium.selenium import *


@Given('imprimir logs consola')
@When('imprimir logs consola')
@Then('imprimir logs consola')
def start_brower(context):
    time.sleep(3)
    selenium: Selenium = context.type_driver
    driver: WebDriver = selenium.driver
    Utils.print_info("Error force for print log browser")
    for entry in driver.get_log('browser'):
        print(entry)
    assert 1 == 0
