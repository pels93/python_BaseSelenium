from behave import Given, When, Then
from pages.googlePage import google_Page
from pages.googleResultPage import google_result_search
from driver.typeDriver.selenium.selenium import *

# mod selenium
selenium: Selenium


@Given('Encender el navegador')
def startBrower(context):
    global selenium
    selenium = context.type_driver


@When('El navegador introduce la URL "{web}"')
def step_impl(context, web):
    selenium.utilsDriver.browser_go_to(web)


@When('Se visualiza la pagina de busqueda de google')
def step_impl(context):
    selenium.utilsDriver.sleep(1)


@When('Buscar en google por "{web}"')
def step_impl(context, web):
    google = google_Page(selenium)
    google.barra.send_keys(web)
    google.barra.submit()


@When('se abre una segunda ventana')
def step_impl(context):
    selenium.utilsDriver.open_new_tab()


@When('se selecciona la "{indice}" pestana')
def step_impl(context, indice):
    selenium.utilsDriver.change_tab(int(indice))


@When('se cierra la pestana "{indice}"')
def step_impl(context, indice):
    selenium.utilsDriver.change_tab(int(indice))
    selenium.utilsDriver.close()


@When('Seleccionar el primer resultado en google')
def step_impl(context):
    selenium.utilsDriver.sleep(2)
    result = google_result_search(selenium)
    result.resultFirst.click()


@Then('Comprobar que lleva a "{url}"')
def step_impl(context, url):
    selenium.utilsDriver.sleep(2)
    selenium.utilsWebElements.assert_containt_text(url, selenium.utilsDriver.get_browser_url(), True)
