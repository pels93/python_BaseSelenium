from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.edge.webdriver import WebDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge


class LauchEdge():

    def start(self) -> WebDriver:
        return Edge(executable_path=EdgeChromiumDriverManager().install(),capabilities=self._set_capabilities_(),options=self._set_options_())


    def _set_capabilities_(self):
        capabilities = DesiredCapabilities.EDGE.copy()
        capabilities['acceptInsecureCerts'] = True
        capabilities['acceptSslCerts'] = True
        capabilities['ACCEPT_SSL_CERTS'] = True
        capabilities['ACCEPT_INSECURE_CERTS'] = True
        capabilities['webdriver_accept_untrusted_certs'] = True
        capabilities['webdriver_assume_untrusted_issuer'] = True
        return capabilities

    def _set_options_(self):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True  # if we miss this line, we can't make Edge headless
        # A little different from Chrome cause we don't need two lines before 'headless' and 'disable-gpu'
        edge_options.add_argument('headless')
        edge_options.add_argument('disable-gpu')
        return edge_options


