from behave import Given, When, Then

from pages.color_game_Page import ColorGames
from pages.googlePage import GooglePageObject
from pages.googleResultPage import google_result_search
from driver.typeDriver.selenium.selenium import *

# mod selenium
selenium: Selenium


@When('Iniciar juego')
def startBrower(context):
    global selenium, game
    selenium = context.type_driver
    game = ColorGames(selenium)
