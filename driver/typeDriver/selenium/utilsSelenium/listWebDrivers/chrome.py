from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class Chrome():

    def start(self) -> WebDriver:
        return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                desired_capabilities=self._set_capabilities_())

    def _set_capabilities_(self):
        capabilities = DesiredCapabilities.CHROME.copy()
        # print log browser
        capabilities['loggingPrefs'] = {'browser': 'ALL'}
        capabilities['acceptInsecureCerts'] = True
        capabilities['acceptSslCerts'] = True
        capabilities['ACCEPT_SSL_CERTS'] = True
        capabilities['ACCEPT_INSECURE_CERTS'] = True
        capabilities['webdriver_accept_untrusted_certs'] = True
        capabilities['webdriver_assume_untrusted_issuer'] = True
        return capabilities