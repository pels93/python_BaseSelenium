from behave import Given, When, Then
from pages.googlePage import google_Page
from pages.googleResultPage import google_result_search

# mod selenium
selenium = None


@Given('Encender el navegador')
def startBrower(context):
    global selenium
    selenium = context.driver


@When('El navegador introduce la URL "{web}"')
def step_impl(context, web):
    selenium.utilsDriver.browserGoTo(web)


@When('Se visualiza la pagina de busqueda de google')
def step_impl(context):
    selenium.utilsDriver.sleep(1)


@When('Buscar en google por "{web}"')
def step_impl(context, web):
    google = google_Page(selenium)
    google.barra.send_keys(web)
    google.barra.submit()


@When('Seleccionar el primer resultado en google')
def step_impl(context):
    selenium.utilsDriver.sleep(2)
    result = google_result_search(selenium)
    result.resultFirst.click()


@Then('Comprobar que lleva a "{url}"')
def step_impl(context, url):
    selenium.utilsDriver.sleep(2)
    selenium.utilsWebElements.assertEqualText(url, selenium.utilsDriver.getBrowserUrl(), True)
