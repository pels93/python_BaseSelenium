from behave import Given, When, Then
from pages.googlePage import GooglePageObject
from pages.googleResultPage import google_result_search
from driver.typeDriver.selenium.selenium import *

# mod selenium
selenium: Selenium


@Given('Encender el navegador')
@When('Encender el navegador')
@Then('Encender el navegador')
def startBrower(context):
    global selenium
    selenium = context.type_driver


@Given('El navegador introduce la URL "{web}"')
@When('El navegador introduce la URL "{web}"')
@Then('El navegador introduce la URL "{web}"')
def step_impl(context, web):
    selenium.utilsDriver.browser_go_to(web)


@Given('El navegador espera "{seconds}" segundos')
@When('El navegador espera "{seconds}" segundos')
@Then('El navegador espera "{seconds}" segundos')
def step_impl(context, seconds):
    selenium.utilsDriver.sleep(int(seconds))


@Given('Se visualiza la pagina de busqueda de google')
@When('Se visualiza la pagina de busqueda de google')
@Then('Se visualiza la pagina de busqueda de google')
def step_impl(context):
    selenium.utilsDriver.sleep(1)


@Given('Buscar en google por "{web}"')
@When('Buscar en google por "{web}"')
@Then('Buscar en google por "{web}"')
def step_impl(context, web):
    google = GooglePageObject(selenium)
    google.barra.send_keys(web)
    google.barra.submit()


@Given('se abre una nueva pestana')
@When('se abre una nueva pestana')
@Then('se abre una nueva pestana')
def step_impl(context):
    selenium.utilsDriver.open_new_tab()


@Given('se selecciona la "{indice}" pestana')
@When('se selecciona la "{indice}" pestana')
@Then('se selecciona la "{indice}" pestana')
def step_impl(context, indice):
    selenium.utilsDriver.change_tab(int(indice))


@Given('se cierra la pestana "{indice}"')
@When('se cierra la pestana "{indice}"')
@Then('se cierra la pestana "{indice}"')
def step_impl(context, indice):
    selenium.utilsDriver.change_tab(int(indice))
    selenium.utilsDriver.close()


@Given('Seleccionar el primer resultado en google')
@When('Seleccionar el primer resultado en google')
@Then('Seleccionar el primer resultado en google')
def step_impl(context):
    selenium.utilsDriver.sleep(2)
    result = google_result_search(selenium)
    result.resultFirst.click()


@Given('Comprobar que lleva a "{url}"')
@When('Comprobar que lleva a "{url}"')
@Then('Comprobar que lleva a "{url}"')
def step_impl(context, url):
    selenium.utilsDriver.sleep(2)
    selenium.utilsWebElements.assert_equal_text(url, selenium.utilsDriver.get_browser_url(), True)
