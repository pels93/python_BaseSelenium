from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.opera.options import Options


class Opera:

    def start(self) -> WebDriver:
        return webdriver.Opera(executable_path=OperaDriverManager().install(),
                               desired_capabilities=self._set_capabilities_(), options=self._set_options_())

    def _set_capabilities_(self):
        capabilities = DesiredCapabilities.OPERA.copy()
        capabilities['acceptInsecureCerts'] = True
        capabilities['acceptSslCerts'] = True
        capabilities['ACCEPT_SSL_CERTS'] = True
        capabilities['ACCEPT_INSECURE_CERTS'] = True
        capabilities['webdriver_accept_untrusted_certs'] = True
        capabilities['webdriver_assume_untrusted_issuer'] = True
        return capabilities

    def _set_options_(self):
        options = Options()
        options.headless = True
        return options
