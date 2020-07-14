from driver import StartTypeDriver
from pages.googlePage import google_Page
from pages.googleResultPage import google_result_search

auxini_selenium = StartTypeDriver.StartDriver()
selenium = auxini_selenium.selenium
selenium.utilsDriver.browser_go_to("https://www.google.es")
google = google_Page(selenium)
barra = google.barra
barra.send_keys("amazon")
barra.submit()
selenium.utilsDriver.sleep(5)
result = google_result_search(selenium)
result.resultFirst.click()
selenium.utilsDriver.wait(20)
selenium.utilsDriver.sleep(2)
a = selenium.utilsDriver.get_browser_url()
selenium.utilsWebElements.assertEqualText(a, "htttps:www", False)
