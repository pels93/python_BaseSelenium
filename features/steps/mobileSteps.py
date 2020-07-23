from behave import Given, When, Then
from pages.mobile import mobile_page

# mod appium
appium = None
mobile = None


@Given('AppMobile Cerrar Popup')
def startmobile(context):
    global appium, mobile
    appium = context.type_driver
    mobile = mobile_page(appium)
    mobile.popup()
    mobile.el1[0].click()


@Given('Comprobar fecha')
def date(context):
    print("pendiente")


@When('comprueba todos los botones')
def testbuttoncalculate(context):
    mobile.findElements()
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num0, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num1, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num2, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num3, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num4, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num5, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num6, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num7, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num8, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.num9, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.suma, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.resta, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(
        mobile.multiplicacion, False)
    appium.utilsMobileElements.assertIsDisplayOrEnanble(mobile.division, False)


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
def startBrower(context, numero):
    appium.utilsMobileElements.pressLongElement(mobile.pantalla, 2000)
    mobile.findResult()
    textResult = str(mobile.result.text)
    textResult = textResult[textResult.find('"') + 1:textResult.rfind('"')]
    appium.utilsMobileElements.assertEqualText(textResult, str(0), False)