from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class Chrome():

    def start(self) -> WebDriver:
        return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                desired_capabilities=self._set_capabilities_(), options=self._set_options_())

    def _set_capabilities_(self):
        capabilities = DesiredCapabilities.CHROME.copy()
        # print log browser
        capabilities['loggingPrefs'] = {'browser': 'ALL'}
        # accept certificates
        capabilities['acceptInsecureCerts'] = True
        capabilities['acceptSslCerts'] = True
        capabilities['ACCEPT_SSL_CERTS'] = True
        capabilities['ACCEPT_INSECURE_CERTS'] = True
        capabilities['webdriver_accept_untrusted_certs'] = True
        capabilities['webdriver_assume_untrusted_issuer'] = True
        return capabilities

    def _set_options_(self):
        mobile_emulation = {"deviceName": "Nexus 10"}
        opts: Options = Options()
        # disable cors
        opts.add_argument("--disable-web-security")
        # mode mobile
        # opts.experimental_options("mobileEmulation", mobile_emulation)
        opts.headless = True
        return opts
