from driver import StartTypeDriver
from pages.googlePage import google_Page
from pages.googleResultPage import google_result_search
from driver.typeDriver.selenium.selenium import *

auxini_selenium = StartTypeDriver.StartDriver()
selenium: Selenium = auxini_selenium.selenium
selenium.utilsDriver.browser_go_to("https://www.google.es")
google = google_Page(selenium)
barra = google.barra
barra.send_keys("amazon")
barra.submit()
#new tab
selenium.utilsDriver.open_new_tab()
selenium.utilsDriver.change_tab(1)
selenium.utilsDriver.browser_go_to("https://www.google.es")
google = google_Page(selenium)
barra = google.barra
barra.send_keys("amazon")
selenium.utilsDriver.close()
selenium.utilsDriver.change_tab(0)
#end new tab
selenium.utilsDriver.sleep(5)
result = google_result_search(selenium)
result.resultFirst.click()
selenium.utilsDriver.wait(20)
selenium.utilsDriver.sleep(2)
a = selenium.utilsDriver.get_browser_url()
selenium.utilsWebElements.assert_equal_text(a, "htttps:www", False)
