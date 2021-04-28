from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver


class Edge():

    def start(self) -> WebDriver:
        return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(),capabilities=self._set_capabilities_())


    def _set_capabilities_(self):
        capabilities = DesiredCapabilities.EDGE.copy()
        capabilities['acceptInsecureCerts'] = True
        capabilities['acceptSslCerts'] = True
        capabilities['ACCEPT_SSL_CERTS'] = True
        capabilities['ACCEPT_INSECURE_CERTS'] = True
        capabilities['webdriver_accept_untrusted_certs'] = True
        capabilities['webdriver_assume_untrusted_issuer'] = True
        return capabilities


