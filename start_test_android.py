from driver import StartTypeDriver
from pages.mobile import mobile_page
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import Utils

appium = StartTypeDriver.StartDriver().appium
mobile = mobile_page(appium)
mobile.popup()
if len(mobile.el1) > 0:
    mobile.el1[0].click()
mobile.findElements()
c = 0
while c < 2:
    mobile.num0.click()
    mobile.num1.click()
    mobile.num2.click()
    mobile.num3.click()
    mobile.num4.click()
    mobile.num5.click()
    mobile.num6.click()
    mobile.num7.click()
    mobile.num8.click()
    mobile.num9.click()
    random = Utils.int_random(0, 3)
    if random == 0:
        mobile.suma.click()
    elif random == 1:
        mobile.resta.click()
    elif random == 2:
        mobile.multiplicacion.click()
    else:
        mobile.division.click()
    mobile.num6.click()
    mobile.num7.click()
    mobile.num8.click()
    mobile.num9.click()
    mobile.num0.click()
    mobile.num1.click()
    mobile.num2.click()
    mobile.num3.click()
    mobile.num4.click()
    mobile.num5.click()
    mobile.igual.click()
    mobile.clear()
    mobile.C.click()
    mobile.deletAll()
    mobile.AC.click()
    c += 0
appium.UtilsMobileElements.pressLongElement(mobile.pantalla, 2000)
mobile.findResult()
textResult = str(mobile.result.text)
textResult = textResult[textResult.find('"') + 1:textResult.rfind('"')]
appium.UtilsMobileElements.assertEqualText(textResult, str(0), False)
