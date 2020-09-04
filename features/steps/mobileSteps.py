from behave import Given, When, Then
from pages.mobile import MobilePageObject
from driver.typeDriver.appium.appium import *

# mod appium
appium: Appium
mobile: MobilePageObject


@Given('AppMobile Cerrar Popup')
def start_mobile(context):
    global appium, mobile
    appium: Appium = context.type_driver
    mobile: MobilePageObject = MobilePageObject(appium)
    mobile.popup()
    mobile.el1[0].click()


@Given('Comprobar fecha')
def date(context):
    print("pendiente")


@When('comprueba todos los botones')
def test_button_calculate(context):
    mobile.findElements()
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num0, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num1, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num2, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num3, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num4, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num5, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num6, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num7, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num8, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.num9, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.suma, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.resta, False)
    appium.utilsMobileElements.assert_is_display_or_enable(
        mobile.multiplicacion, False)
    appium.utilsMobileElements.assert_is_display_or_enable(mobile.division, False)


@When('presione el numero "{numero}"')
def press_number_calculate(context, numero):
    count = len(str(numero))
    mobile.findElements()
    for x in range(count):
        if numero[x] == "," or numero[x] == ".":
            mobile.punto.click()
        elif numero[x] == "0":
            mobile.num0.click()
        elif numero[x] == "1":
            mobile.num1.click()
        elif numero[x] == "1":
            mobile.num1.click()
        elif numero[x] == "2":
            mobile.num2.click()
        elif numero[x] == "3":
            mobile.num3.click()
        elif numero[x] == "4":
            mobile.num4.click()
        elif numero[x] == "5":
            mobile.num5.click()
        elif numero[x] == "6":
            mobile.num6.click()
        elif numero[x] == "7":
            mobile.num7.click()
        elif numero[x] == "8":
            mobile.num8.click()
        else:
            mobile.num9.click()


@Then('el resultado tiene que ser "{numero}"')
def step(context, numero):
    appium.utilsMobileElements.pressLongElement(mobile.pantalla, 2000)
    mobile.findResult()
    textResult = str(mobile.result.text)
    textResult = textResult[textResult.find('"') + 1:textResult.rfind('"')]
    appium.utilsMobileElements.assertEqualText(textResult, str(0), False)
