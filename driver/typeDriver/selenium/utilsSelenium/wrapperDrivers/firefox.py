from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


class Firefox():

    def start(self) -> WebDriver:
        return webdriver.Firefox(firefox_profile=self._create_firefox_profile_(),
                                 capabilities=self._set_capabilities_(),
                                 executable_path=GeckoDriverManager().install(), options=self._set_options_())

    def _set_capabilities_(self):
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['acceptInsecureCerts'] = True
        capabilities['acceptSslCerts'] = True
        capabilities['ACCEPT_SSL_CERTS'] = True
        capabilities['ACCEPT_INSECURE_CERTS'] = True
        capabilities['webdriver_accept_untrusted_certs'] = True
        capabilities['webdriver_assume_untrusted_issuer'] = True
        return capabilities

    def _create_firefox_profile_(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = True
        profile.set_preference("browser.link.open_newwindow", 3)
        profile.set_preference("browser.link.open_newwindow.restriction", 0)
        profile.update_preferences()
        return profile

    def _set_options_(self):
        opts: Options = Options()
        opts.headless = True
        return opts
